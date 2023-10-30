; Auto-generated. Do not edit!


(cl:in-package manager-msg)


;//! \htmlinclude SteeringControl.msg.html

(cl:defclass <SteeringControl> (roslisp-msg-protocol:ros-message)
  ((enabled
    :reader enabled
    :initarg :enabled
    :type cl:boolean
    :initform cl:nil)
   (steering_angle
    :reader steering_angle
    :initarg :steering_angle
    :type cl:float
    :initform 0.0))
)

(cl:defclass SteeringControl (<SteeringControl>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SteeringControl>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SteeringControl)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name manager-msg:<SteeringControl> is deprecated: use manager-msg:SteeringControl instead.")))

(cl:ensure-generic-function 'enabled-val :lambda-list '(m))
(cl:defmethod enabled-val ((m <SteeringControl>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader manager-msg:enabled-val is deprecated.  Use manager-msg:enabled instead.")
  (enabled m))

(cl:ensure-generic-function 'steering_angle-val :lambda-list '(m))
(cl:defmethod steering_angle-val ((m <SteeringControl>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader manager-msg:steering_angle-val is deprecated.  Use manager-msg:steering_angle instead.")
  (steering_angle m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SteeringControl>) ostream)
  "Serializes a message object of type '<SteeringControl>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'enabled) 1 0)) ostream)
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'steering_angle))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SteeringControl>) istream)
  "Deserializes a message object of type '<SteeringControl>"
    (cl:setf (cl:slot-value msg 'enabled) (cl:not (cl:zerop (cl:read-byte istream))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'steering_angle) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SteeringControl>)))
  "Returns string type for a message object of type '<SteeringControl>"
  "manager/SteeringControl")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SteeringControl)))
  "Returns string type for a message object of type 'SteeringControl"
  "manager/SteeringControl")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SteeringControl>)))
  "Returns md5sum for a message object of type '<SteeringControl>"
  "b4bc179aa9c01f2acacbf2c87950c45d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SteeringControl)))
  "Returns md5sum for a message object of type 'SteeringControl"
  "b4bc179aa9c01f2acacbf2c87950c45d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SteeringControl>)))
  "Returns full string definition for message of type '<SteeringControl>"
  (cl:format cl:nil "bool enabled~%float32 steering_angle~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SteeringControl)))
  "Returns full string definition for message of type 'SteeringControl"
  (cl:format cl:nil "bool enabled~%float32 steering_angle~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SteeringControl>))
  (cl:+ 0
     1
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SteeringControl>))
  "Converts a ROS message object to a list"
  (cl:list 'SteeringControl
    (cl:cons ':enabled (enabled msg))
    (cl:cons ':steering_angle (steering_angle msg))
))
