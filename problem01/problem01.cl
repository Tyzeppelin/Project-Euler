
(defun factor_3_or_5 (n) 
  (cond
    ((= (mod n 3) 0) n)
    ((= (mod n 5) 0) n)
    (t 0)
))

(defun main_loop (n acc)
  (if (< n 3) acc (main_loop (- n 1) (+ acc (factor_3_or_5 n))))
)

(write (main_loop 999 0))
