
(defun app (ll x)
  (if (car ll) (cons (car ll) (app (cdr ll) x)) (cons x nil))
)

(defun n-th-prime (n) 
    (labels
      (
        (is-prime (n p-array)
          (cond 
            ((eq p-array nil) t)
            ((> (car p-array) (sqrt n)) t)
            ((= (mod n (car p-array)) 0) nil)
            (t (is-prime n (cdr p-array)))
        ))
        (inner-nth-p (n i p-array sum-primes)
          (cond ((<= n i) sum-primes)
                ((is-prime i p-array) (inner-nth-p n (+ i 2) (if (< i (sqrt n)) (app p-array i) p-array) (+ sum-primes i)))
                (t (inner-nth-p n (+ i 2) p-array sum-primes))
        )))
      (inner-nth-p n 3 (cons 2 nil) 2)
  )
)

(defun main ()

  (n-th-prime 2000000)
)

(time (write (main)))
