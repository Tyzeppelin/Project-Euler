
(defun app (ll x)
  (if (car ll) (cons (car ll) (app (cdr ll) x)) (cons x nil))
)

(defun n-th-prime (n) 
    (labels
      (
        (is-prime (n p-array)
          (cond 
            ((eq p-array nil) t)
            ;((> (car p-array) n) t)
            ((> (car p-array) (sqrt n)) t)
            ((= (mod n (car p-array)) 0) nil)
            (t (is-prime n (cdr p-array)))
        ))
        (inner-nth-p (n i acc)
          (cond ((= n 0) (last acc))
                ((is-prime i acc) (inner-nth-p (- n 1) (+ i 2) (app acc i)))
                (t (inner-nth-p n (+ i 2) acc))
        )))
      (inner-nth-p n 3 '(2))
  )
)

(defun main ()

  (n-th-prime 10001)
)

(time (write (main)))
