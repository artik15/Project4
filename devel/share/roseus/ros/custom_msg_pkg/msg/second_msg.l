;; Auto-generated. Do not edit!


(when (boundp 'custom_msg_pkg::second_msg)
  (if (not (find-package "CUSTOM_MSG_PKG"))
    (make-package "CUSTOM_MSG_PKG"))
  (shadow 'second_msg (find-package "CUSTOM_MSG_PKG")))
(unless (find-package "CUSTOM_MSG_PKG::SECOND_MSG")
  (make-package "CUSTOM_MSG_PKG::SECOND_MSG"))

(in-package "ROS")
;;//! \htmlinclude second_msg.msg.html


(defclass custom_msg_pkg::second_msg
  :super ros::object
  :slots (_start_time _msg_seq _original_num _square_num _sqrt_num ))

(defmethod custom_msg_pkg::second_msg
  (:init
   (&key
    ((:start_time __start_time) (instance ros::time :init))
    ((:msg_seq __msg_seq) 0)
    ((:original_num __original_num) 0)
    ((:square_num __square_num) 0.0)
    ((:sqrt_num __sqrt_num) 0.0)
    )
   (send-super :init)
   (setq _start_time __start_time)
   (setq _msg_seq (round __msg_seq))
   (setq _original_num (round __original_num))
   (setq _square_num (float __square_num))
   (setq _sqrt_num (float __sqrt_num))
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
  (:square_num
   (&optional __square_num)
   (if __square_num (setq _square_num __square_num)) _square_num)
  (:sqrt_num
   (&optional __sqrt_num)
   (if __sqrt_num (setq _sqrt_num __sqrt_num)) _sqrt_num)
  (:serialization-length
   ()
   (+
    ;; time _start_time
    8
    ;; uint16 _msg_seq
    2
    ;; uint16 _original_num
    2
    ;; float32 _square_num
    4
    ;; float32 _sqrt_num
    4
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
     ;; float32 _square_num
       (sys::poke _square_num (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _sqrt_num
       (sys::poke _sqrt_num (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
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
   ;; float32 _square_num
     (setq _square_num (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _sqrt_num
     (setq _sqrt_num (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get custom_msg_pkg::second_msg :md5sum-) "72b9852d7e6f83455e011ab1603aed70")
(setf (get custom_msg_pkg::second_msg :datatype-) "custom_msg_pkg/second_msg")
(setf (get custom_msg_pkg::second_msg :definition-)
      "time start_time
uint16 msg_seq
uint16 original_num
float32 square_num
float32 sqrt_num

")



(provide :custom_msg_pkg/second_msg "72b9852d7e6f83455e011ab1603aed70")


