
;(defun gen-coprime (n) 
;  (labels (
;    (b1 (m n) ())
;    ())
;    ()
;))

;(defun are-integers (ln)
;  (if (typep (car ln) 'integer) (are-integers (cdr ln)) nil)
;)

(defun prod-pyth-trip (n i j)
  (let* ((x (* i j))
        (y (/ (- (* i i) (* j j)) 2))
        (z (/ (+ (* i i) (* j j)) 2))
        (x-y-z (+ x y z)))
    (cond ((= x-y-z n) (* x y z))
          ((> x-y-z n) (prod-pyth-trip n (+ j 2) (1+ j)))
          (t (prod-pyth-trip n (1+ i) j))
)))


(defun main ()
  (gen-pyth-trip 1000 2 1)
)

(time (write (main)))
