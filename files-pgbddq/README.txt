These are a collection of QBF files for the linear domino benchmark
(.qcnf), along with files specifying the BDD variable ordering
(.order)

Files are named ldomino-N-winX-TF-POS.qcnf, with
      N:   Size of the board
      X:   Is A the winner or B?
      TF:  Is the formula true or false?
      POS: Are definition variables placed after their defining variables or at the end?

Running ./generate.sh will generate the benchmark files.
