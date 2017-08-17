
(defun is-pal (n) 
  (let ((n-list (map 'list #'digit-char-p (prin1-to-string n))))
    (equal n-list (reverse n-list))
))

(defun naive (x)
  (defun inner (y) 
    (if (= y 1) nil
      (if (is-pal (* x y))
        (cons (* x y) (inner (- y 1)))
        (cons 0 (inner (- y 1)))
  )))
  (if (= x 1) 0
    (max (reduce #'max (inner x)) (naive (- x 1)))
))

(defun main () (naive 999))
(time (write (main)))
