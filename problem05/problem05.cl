
(defun first-div (n d) 
  (if (= (mod n d) 0) d 
    (first-div n (+ d 1))
))

(defun prime-div (n last-div)
  (if (< n last-div) nil 
    (let ((res (first-div n last-div)))
      (cons res (prime-div (/ n res) res))
)))

; todo utiliser des booleens
(defun not-in-list (in fac)
  (labels 
    ((is-in (x l)
      (if l 
        (if (= (car l) x) nil 
          (is-in x (cdr l)))
        x
  )))
    (if in 
      (let ((n (is-in (car in) fac)))
        (if n (cons n (not-in-list (cdr in) fac))
          (cons nil (not-in-list (cdr in) (remove (car fac) fac :count 1)))))
      nil
)))

(defun all-divisors (n acc)
  (if (<= n 1) acc
    (all-divisors (- n 1) (append acc (remove nil (not-in-list (prime-div n 2) acc))))
))

(defun prod-all-div (n)
  (reduce #'* (all-divisors n nil))
)

; 51s
;(defvar n 100000)

(defvar n 20)

(defun main ()
;  (prime-div 232792560 2)
;  (write (prime-div 8 2))
;  (terpri)
;  (write (prime-div n 2))
;  (terpri)
;  (write (all-divisors n nil))
;  (terpri)
  (prod-all-div n)
)

(time (write (main)))
