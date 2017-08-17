
;defun memoize (fn)
;  (let ((cache (make-hash-table :test #'equal)))
;    #'(lambda (&rest args) 
;          (multiple-value-bind
;            (result exists)
;            (gethash args cache)
;            (if exists result
;              (setf (gethash args cache) (apply fn args))
;))))

(defun naive-fibo (n f0 f1 acc)
  (if (<= n f0) acc
    (naive-fibo (- n 1) f1 (+ f0 f1) (if (evenp f1) (+ acc f1) acc))
))

(defun main () 
  (naive-fibo 4000000 1 1 0)
) 


(write (main))
