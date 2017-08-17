
(defun first-div (n d) 
  (if (= (mod n d) 0) d 
    (first-div n (+ d 2))
))

(defun biggest-prime-div (n last-div)
  (if (< n last-div) last-div
    (let ((res (first-div n last-div)))
      (biggest-prime-div (/ n res) res)
)))

(defun main () 
  (biggest-prime-div 600851475143 3)
)

(write (main))
