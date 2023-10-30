; Auto-generated. Do not edit!


(cl:in-package manager-msg)


;//! \htmlinclude SpeedControl.msg.html

(cl:defclass <SpeedControl> (roslisp-msg-protocol:ros-message)
  ((enabled
    :reader enabled
    :initarg :enabled
    :type cl:boolean
    :initform cl:nil)
   (speed
    :reader speed
    :initarg :speed
    :type cl:float
    :initform 0.0))
)

(cl:defclass SpeedControl (<SpeedControl>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SpeedControl>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SpeedControl)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name manager-msg:<SpeedControl> is deprecated: use manager-msg:SpeedControl instead.")))

(cl:ensure-generic-function 'enabled-val :lambda-list '(m))
(cl:defmethod enabled-val ((m <SpeedControl>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader manager-msg:enabled-val is deprecated.  Use manager-msg:enabled instead.")
  (enabled m))

(cl:ensure-generic-function 'speed-val :lambda-list '(m))
(cl:defmethod speed-val ((m <SpeedControl>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader manager-msg:speed-val is deprecated.  Use manager-msg:speed instead.")
  (speed m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SpeedControl>) ostream)
  "Serializes a message object of type '<SpeedControl>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'enabled) 1 0)) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'speed))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SpeedControl>) istream)
  "Deserializes a message object of type '<SpeedControl>"
    (cl:setf (cl:slot-value msg 'enabled) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'speed) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SpeedControl>)))
  "Returns string type for a message object of type '<SpeedControl>"
  "manager/SpeedControl")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SpeedControl)))
  "Returns string type for a message object of type 'SpeedControl"
  "manager/SpeedControl")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SpeedControl>)))
  "Returns md5sum for a message object of type '<SpeedControl>"
  "959738decaba41841790fb595d10b1d5")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SpeedControl)))
  "Returns md5sum for a message object of type 'SpeedControl"
  "959738decaba41841790fb595d10b1d5")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SpeedControl>)))
  "Returns full string definition for message of type '<SpeedControl>"
  (cl:format cl:nil "bool enabled~%float32 speed~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SpeedControl)))
  "Returns full string definition for message of type 'SpeedControl"
  (cl:format cl:nil "bool enabled~%float32 speed~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SpeedControl>))
  (cl:+ 0
     1
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SpeedControl>))
  "Converts a ROS message object to a list"
  (cl:list 'SpeedControl
    (cl:cons ':enabled (enabled msg))
    (cl:cons ':speed (speed msg))
))
