;; Auto-generated. Do not edit!


(when (boundp 'manager::manager)
  (if (not (find-package "MANAGER"))
    (make-package "MANAGER"))
  (shadow 'manager (find-package "MANAGER")))
(unless (find-package "MANAGER::MANAGER")
  (make-package "MANAGER::MANAGER"))

(in-package "ROS")
;;//! \htmlinclude manager.msg.html


(defclass manager::manager
  :super ros::object
  :slots (_enabled _speed ))

(defmethod manager::manager
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

(setf (get manager::manager :md5sum-) "959738decaba41841790fb595d10b1d5")
(setf (get manager::manager :datatype-) "manager/manager")
(setf (get manager::manager :definition-)
      "bool enabled
float32 speed
")



(provide :manager/manager "959738decaba41841790fb595d10b1d5")


