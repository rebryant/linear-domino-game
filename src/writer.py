#####################################################################################
# Copyright (c) 2022 Marijn Heule, Randal E. Bryant, Carnegie Mellon University
# Last edit: March 23, 2022
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
# associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute,
# sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all copies or
# substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT
# NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT
# OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
########################################################################################

# Code for generating QCNF, orders, and clusters
class WriterException(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "Writer Exception: " + str(self.value)


# Generic writer
class Writer:
    outfile = None
    verbose = False
    variableCount = None

    def __init__(self, outfile, verbose = False):
        self.variableCount = 0
        self.outfile = outfile
        self.verbose = verbose

    def countVariables(self, count):
        self.variableCount += count

    def trim(self, line):
        while len(line) > 0 and line[-1] == '\n':
            line = line[:-1]
        return line

    def show(self, line):
        line = self.trim(line)
        if self.verbose:
            print(line)
        if self.outfile is not None:
            self.outfile.write(line + '\n')

    def finish(self):
        if self.outfile is None:
            return
        self.outfile.close()
        self.outfile = None


# Creating QCNF
class QcnfWriter(Writer):
    clauseCount = 0
    outputList = []
    # Quantification type for each level
    quantifications = {}
    # Mapping from level to list of variables
    variableLists = {}
    # List of comments for each level of variables
    variableCommentLists = {}

    def __init__(self, outfile, verbose = False):
        Writer.__init__(self, outfile, verbose = verbose)
        self.clauseCount = 0
        self.outputList = []
        self.quantifications = {}
        self.variableLists = {}
        self.varableCommentLists = {}

    # With CNF, must accumulate all of the clauses, since the file header
    # requires providing the number of clauses.

    def addVariables(self, level, vlist, isExistential):
        self.countVariables(len(vlist))
        if level in self.quantifications:
            if self.quantifications[level] != isExistential:
                print("Attempting to add variables %s.  Quantification %s" % (str(vlist), "existential" if isExistential else "universal"))
                print("Existing variables at level %d: %s.  Quantification %s" % (level, str(self.variableLists[level]), "existential" if self.quantifications[level] else "universal"))
                raise WriterException("Attempt different quantifications at level %d" % level)
            self.variableLists[level] += vlist
        else:
            self.quantifications[level] = isExistential
            self.variableLists[level] = list(vlist)

    def addVariable(self, level, var, isExistential):
        self.countVariables(1)
        if level in self.quantifications:
            if self.quantifications[level] != isExistential:
                print("Attempting to add variable %d.  Quantification %s" % (var, "existential" if isExistential else "universal"))
                print("Existing variables at level %d: %s.  Quantification %s" % (level, str(self.variableLists[level]), "existential" if self.quantifications[level] else "universal"))
                raise WriterException("Attempt different quantifications at level %d" % level)
            self.variableLists[level].append(var)
        else:
            self.quantifications[level] = isExistential
            self.variableLists[level] = [var]

            
    def doComment(self, line):
        self.outputList.append("c " + line)

    def doVariableComment(self, level, line):
        if level not in self.variableCommentLists:
            self.variableCommentLists[level] = []
        self.variableCommentLists[level].append(line)

    def doClause(self, literals):
        ilist = literals + [0]
        self.clauseCount += 1
        self.outputList.append(" ".join([str(i) for i in ilist]))

    # Compress the set of levels so that have strict alternation
    def compressLevels(self):
        levels = sorted(self.quantifications.keys())
        if len(levels) == 0:
            return
        if levels[0] == -1:
            # Move undesignated variables to innermost level
            levels = levels[1:] + [-1]
        newLevel = 0
        oldLevel = levels[0]
        newQuantifications = { newLevel : self.quantifications[oldLevel] }
        newVariableLists = { newLevel : self.variableLists[oldLevel]}
        if oldLevel in self.variableCommentLists:
            newVariableCommentLists = { newLevel : self.variableCommentLists[oldLevel] }
        else:
            newVariableCommentLists = { newLevel : [] }
        for oldLevel in levels[1:]:
            if self.quantifications[oldLevel] == newQuantifications[newLevel]:
                newVariableLists[newLevel] += self.variableLists[oldLevel]
            else:
                newLevel += 1
                newQuantifications[newLevel] = self.quantifications[oldLevel]
                newVariableLists[newLevel] = self.variableLists[oldLevel]
                newVariableCommentLists[newLevel] = []
            if oldLevel in self.variableCommentLists:
                newVariableCommentLists[newLevel] += self.variableCommentLists[oldLevel]

        self.quantifications = newQuantifications
        self.variableLists = newVariableLists
        self.variableCommentLists = newVariableCommentLists

    def finish(self):
        if self.outfile is None:
            return
        self.show("p cnf %d %d" % (self.variableCount, self.clauseCount))
        self.compressLevels()
        levels = sorted(self.quantifications.keys())
        if len(levels) > 0 and levels[0] == -1:
            # Move undesignated variables to innermost level
            levels = levels[1:] + [-1]
        for level in levels:
            if level in self.variableCommentLists:
                for line in self.variableCommentLists[level]:
                    self.show("c " + line + '\n')
            qchar = 'e' if self.quantifications[level] else 'a'
            slist = [str(v) for v in self.variableLists[level]]
            line = qchar + ' ' + ' '.join(slist) + ' 0'
            self.show(line)
        for line in self.outputList:
            self.show(line)
        self.outfile.close()
        self.outfile = None
    

# Generate variable ordering for BDD-based solver
class OrderWriter(Writer):
    variableList = []

    def __init__(self, count, outfile, verbose = False):
        Writer.__init__(self, outfile, verbose = verbose)
        self.countVariables(count)
        self.variableList = []

    def doOrder(self, vlist):
        self.show(" ".join([str(c) for c in vlist]))        
        self.variableList += vlist

    def finish(self):
        if self.variableCount != len(self.variableList):
            print("Warning: Incorrect number of variables in ordering")
            print("  Expected %d.  Got %d" % (self.variableCount, len(self.variableList)))

        expected = range(1, self.variableCount+1)
        self.variableList.sort()
        for (e, a) in zip(expected, self.variableList):
            if e != a:
               raise WriterException("Mismatch in ordering.  Expected %d.  Got %d" % (e, a))
        self.writer.finish(self)
