
(defun str-split (str &optional (del " ") (acc nil))
  (let ((cut (position del str :from-end t :test #'string-equal)))
    (if cut (str-split (subseq str 0 cut) del (cons (subseq str (1+ cut)) acc))
      (cons str acc)
)))

; ranges are integers inthe interleave [beg; end]
(defun range (beg end &optional (acc nil))
  (cond
    ((= beg end) (cons beg acc))
    ((> beg end) (reverse (range (1+ end) (1+ beg))))
    (t (range beg (- end 1) (cons end acc)))
))

(defvar *l1* (map 'list #'parse-integer (str-split "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08" " ")))
(defvar *l2* (map 'list #'parse-integer (str-split "49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00" " ")))
(defvar *l3* (map 'list #'parse-integer (str-split "81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65" " ")))
(defvar *l4* (map 'list #'parse-integer (str-split "52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91" " ")))
(defvar *l5* (map 'list #'parse-integer (str-split "22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80" " ")))
(defvar *l6* (map 'list #'parse-integer (str-split "24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50" " ")))
(defvar *l7* (map 'list #'parse-integer (str-split "32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70" " ")))
(defvar *l8* (map 'list #'parse-integer (str-split "67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21" " ")))
(defvar *l9* (map 'list #'parse-integer (str-split "24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72" " ")))
(defvar *la* (map 'list #'parse-integer (str-split "21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95" " ")))
(defvar *lb* (map 'list #'parse-integer (str-split "78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92" " ")))
(defvar *lc* (map 'list #'parse-integer (str-split "16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57" " ")))
(defvar *ld* (map 'list #'parse-integer (str-split "86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58" " ")))
(defvar *le* (map 'list #'parse-integer (str-split "19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40" " ")))
(defvar *lf* (map 'list #'parse-integer (str-split "04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66" " ")))
(defvar *lg* (map 'list #'parse-integer (str-split "88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69" " ")))
(defvar *lh* (map 'list #'parse-integer (str-split "04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36" " ")))
(defvar *li* (map 'list #'parse-integer (str-split "20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16" " ")))
(defvar *lj* (map 'list #'parse-integer (str-split "20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54" " ")))
(defvar *lk* (map 'list #'parse-integer (str-split "01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48" " ")))


(defvar *mat* (make-array '(20 20) :initial-contents (list *l1* *l2* *l3* *l4* *l5* *l6* *l7* *l8* *l9* *la* *lb* *lc* *ld* *le* *lf* *lg* *lh* *li* *lj* *lk*)))

(defvar *vert* (make-array '(20 20) :initial-element 1))
(defvar *hori* (make-array '(20 20) :initial-element 1))
(defvar *dia1* (make-array '(20 20) :initial-element 1))
(defvar *dia2* (make-array '(20 20) :initial-element 1))

(defun update-hv (mat i j value)
  (when i
  (labels (
    (update-y (j)
      (when j
        (let ((old (aref mat (car i) (car j))))
            (setf (aref mat (car i) (car j)) (* old value))
          (update-y (cdr j))
        ))))
    (update-y j) (update-hv mat (cdr i) j value))
))

(defun update-di (mat i j value)
  (when (and i j)
    (let ((old (aref mat (car i) (car j))))
      (setf (aref mat (car i) (car j)) (* old value)) (update-di mat (cdr i) (cdr j) value))
))

(defun parse-mat (mat &optional (i 0) (j 0))
  (when (not (= i 20))
    (if (= j 20) (parse-mat mat (1+ i) 0)
    (let*
      ((value (aref mat i j)))
      (update-hv *vert* (range (max 0 (- i 3)) i) (list j) value)
      (update-hv *hori* (list i) (range (max 0 (- j 3)) j) value)
      (update-di *dia1* (range (max 0 (- i 3)) i) (range (max 0 (- j 3)) j) value)
      (update-di *dia2* (range (max 0 (- i 3)) i) (range j (min 19 (+ j 3))) value)
      (parse-mat mat i (1+ j))
))))

(defun max-arr (arr i j &optional (m 0))
  (cond
    ((= j 0) (max-arr arr (- i 1) 19 m))
    ((= i 0) m)
    (t (max-arr arr i (- j 1) (max m (aref arr i j))))
))


(defun main ()
  *mat*
  (terpri)
  (range 0 10)
  (parse-mat *mat*)
  ;(setf (aref *dia1* 0 0) 1)
  ;(setf (aref *dia1* 1 1) 1)
  ;(write *vert*)
  ;(write *hori*)
  (terpri)
  ;(let
  ;  ((v (max-arr *vert* 19 19))
  ;  (h (max-arr *hori* 19 19))
  ;  (d1 (max-arr *dia1* 19 19))
  ;  (d2 (max-arr *dia2* 19 19)))

  ;  (max v h d1 d2)
  ;)
  ;(write (max-arr *vert* 19 19))
  ;(terpri)
  ;(write (max-arr *hori* 19 19))
  ;(terpri)
  ;(write (max-arr *dia1* 19 19))
  ;(terpri)
  ;(max-arr *dia2* 19 19)
  *dia1*
)

(time (write (main)))
