;; Auto-generated. Do not edit!


(when (boundp 'manager::SpeedControl)
  (if (not (find-package "MANAGER"))
    (make-package "MANAGER"))
  (shadow 'SpeedControl (find-package "MANAGER")))
(unless (find-package "MANAGER::SPEEDCONTROL")
  (make-package "MANAGER::SPEEDCONTROL"))

(in-package "ROS")
;;//! \htmlinclude SpeedControl.msg.html


(defclass manager::SpeedControl
  :super ros::object
  :slots (_enabled _speed ))

(defmethod manager::SpeedControl
  (:init
   (&key
    ((:enabled __enabled) nil)
    ((:speed __speed) 0.0)
    )
   (send-super :init)
   (setq _enabled __enabled)
   (setq _speed (float __speed))
   self)
  (:enabled
   (&optional (__enabled :null))
   (if (not (eq __enabled :null)) (setq _enabled __enabled)) _enabled)
  (:speed
   (&optional __speed)
   (if __speed (setq _speed __speed)) _speed)
  (:serialization-length
   ()
   (+
    ;; bool _enabled
    1
    ;; float32 _speed
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _enabled
       (if _enabled (write-byte -1 s) (write-byte 0 s))
     ;; float32 _speed
       (sys::poke _speed (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _enabled
     (setq _enabled (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; float32 _speed
     (setq _speed (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get manager::SpeedControl :md5sum-) "959738decaba41841790fb595d10b1d5")
(setf (get manager::SpeedControl :datatype-) "manager/SpeedControl")
(setf (get manager::SpeedControl :definition-)
      "bool enabled
float32 speed
")



(provide :manager/SpeedControl "959738decaba41841790fb595d10b1d5")


