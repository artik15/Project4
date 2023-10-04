;; Auto-generated. Do not edit!


(when (boundp 'custom_msg_pkg::first_msg)
  (if (not (find-package "CUSTOM_MSG_PKG"))
    (make-package "CUSTOM_MSG_PKG"))
  (shadow 'first_msg (find-package "CUSTOM_MSG_PKG")))
(unless (find-package "CUSTOM_MSG_PKG::FIRST_MSG")
  (make-package "CUSTOM_MSG_PKG::FIRST_MSG"))

(in-package "ROS")
;;//! \htmlinclude first_msg.msg.html


(defclass custom_msg_pkg::first_msg
  :super ros::object
  :slots (_start_time _msg_seq _original_num ))

(defmethod custom_msg_pkg::first_msg
  (:init
   (&key
    ((:start_time __start_time) (instance ros::time :init))
    ((:msg_seq __msg_seq) 0)
    ((:original_num __original_num) 0)
    )
   (send-super :init)
   (setq _start_time __start_time)
   (setq _msg_seq (round __msg_seq))
   (setq _original_num (round __original_num))
   self)
  (:start_time
   (&optional __start_time)
   (if __start_time (setq _start_time __start_time)) _start_time)
  (:msg_seq
   (&optional __msg_seq)
   (if __msg_seq (setq _msg_seq __msg_seq)) _msg_seq)
  (:original_num
   (&optional __original_num)
   (if __original_num (setq _original_num __original_num)) _original_num)
  (:serialization-length
   ()
   (+
    ;; time _start_time
    8
    ;; uint16 _msg_seq
    2
    ;; uint16 _original_num
    2
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; time _start_time
       (write-long (send _start_time :sec) s) (write-long (send _start_time :nsec) s)
     ;; uint16 _msg_seq
       (write-word _msg_seq s)
     ;; uint16 _original_num
       (write-word _original_num s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; time _start_time
     (send _start_time :sec (sys::peek buf ptr- :integer)) (incf ptr- 4)  (send _start_time :nsec (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; uint16 _msg_seq
     (setq _msg_seq (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; uint16 _original_num
     (setq _original_num (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;;
   self)
  )

(setf (get custom_msg_pkg::first_msg :md5sum-) "4d5888a5a4bca89c6d6a476ac8a88a1a")
(setf (get custom_msg_pkg::first_msg :datatype-) "custom_msg_pkg/first_msg")
(setf (get custom_msg_pkg::first_msg :definition-)
      "time start_time
uint16 msg_seq
uint16 original_num

")



(provide :custom_msg_pkg/first_msg "4d5888a5a4bca89c6d6a476ac8a88a1a")


