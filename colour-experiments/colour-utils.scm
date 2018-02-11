;; Date: 11/02/2018
;; Abhishek Mishra
;;
;; Some basic colour utils for use in turtle programs

(define (make-colour r g b)
  (list r g b))

(define (make-colour-a r g b a)
  (list r g b a))

(define (get-r colour)
  (car colour))

(define (get-g colour)
  (cadr colour))

(define (get-b colour)
  (caddr colour))

(define (get-a colour)
  (cadddr colour))

(define (canvas-colour c)
    (string-append "rgb(" 
                (number->string (get-r c))
                ","
                (number->string (get-g c))
                ","
                (number->string (get-b c))
                ")"))

(define c (make-colour-a 10 20 80 0.2))

;(console-log c)

;(console-log (get-r c))
;(console-log (get-g c))
;(console-log (get-b c))
;(console-log (get-a c))

;(console-log (canvas-colour c))
