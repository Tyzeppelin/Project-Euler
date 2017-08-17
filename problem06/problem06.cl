
(defun sum-of-squares (n sum)
  (if (<= n 0) sum
    (sum-of-squares (- n 1) (+ sum (* n n)))
))

(defun square-of-sum (n sum)
  (if (<= n 0) (* sum sum)
    (square-of-sum (- n 1) (+ sum n))
))

(defun diff (n)
  (- (square-of-sum n 0) (sum-of-squares n 0))
)

(defun main()
  (diff 100)
)

(time (write (main)))
