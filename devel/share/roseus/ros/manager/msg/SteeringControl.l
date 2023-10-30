;; Auto-generated. Do not edit!


(when (boundp 'manager::SteeringControl)
  (if (not (find-package "MANAGER"))
    (make-package "MANAGER"))
  (shadow 'SteeringControl (find-package "MANAGER")))
(unless (find-package "MANAGER::STEERINGCONTROL")
  (make-package "MANAGER::STEERINGCONTROL"))

(in-package "ROS")
;;//! \htmlinclude SteeringControl.msg.html


(defclass manager::SteeringControl
  :super ros::object
  :slots (_enabled _steering_angle ))

(defmethod manager::SteeringControl
  (:init
   (&key
    ((:enabled __enabled) nil)
    ((:steering_angle __steering_angle) 0.0)
    )
   (send-super :init)
   (setq _enabled __enabled)
   (setq _steering_angle (float __steering_angle))
   self)
  (:enabled
   (&optional (__enabled :null))
   (if (not (eq __enabled :null)) (setq _enabled __enabled)) _enabled)
  (:steering_angle
   (&optional __steering_angle)
   (if __steering_angle (setq _steering_angle __steering_angle)) _steering_angle)
  (:serialization-length
   ()
   (+
    ;; bool _enabled
    1
    ;; float32 _steering_angle
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _enabled
       (if _enabled (write-byte -1 s) (write-byte 0 s))
     ;; float32 _steering_angle
       (sys::poke _steering_angle (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _enabled
     (setq _enabled (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; float32 _steering_angle
     (setq _steering_angle (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get manager::SteeringControl :md5sum-) "b4bc179aa9c01f2acacbf2c87950c45d")
(setf (get manager::SteeringControl :datatype-) "manager/SteeringControl")
(setf (get manager::SteeringControl :definition-)
      "bool enabled
float32 steering_angle
")



(provide :manager/SteeringControl "b4bc179aa9c01f2acacbf2c87950c45d")


