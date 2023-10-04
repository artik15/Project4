; Auto-generated. Do not edit!


(cl:in-package custom_msg_pkg-msg)


;//! \htmlinclude first_msg.msg.html

(cl:defclass <first_msg> (roslisp-msg-protocol:ros-message)
  ((start_time
    :reader start_time
    :initarg :start_time
    :type cl:real
    :initform 0)
   (msg_seq
    :reader msg_seq
    :initarg :msg_seq
    :type cl:fixnum
    :initform 0)
   (original_num
    :reader original_num
    :initarg :original_num
    :type cl:fixnum
    :initform 0))
)

(cl:defclass first_msg (<first_msg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <first_msg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'first_msg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name custom_msg_pkg-msg:<first_msg> is deprecated: use custom_msg_pkg-msg:first_msg instead.")))

(cl:ensure-generic-function 'start_time-val :lambda-list '(m))
(cl:defmethod start_time-val ((m <first_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custom_msg_pkg-msg:start_time-val is deprecated.  Use custom_msg_pkg-msg:start_time instead.")
  (start_time m))

(cl:ensure-generic-function 'msg_seq-val :lambda-list '(m))
(cl:defmethod msg_seq-val ((m <first_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custom_msg_pkg-msg:msg_seq-val is deprecated.  Use custom_msg_pkg-msg:msg_seq instead.")
  (msg_seq m))

(cl:ensure-generic-function 'original_num-val :lambda-list '(m))
(cl:defmethod original_num-val ((m <first_msg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custom_msg_pkg-msg:original_num-val is deprecated.  Use custom_msg_pkg-msg:original_num instead.")
  (original_num m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <first_msg>) ostream)
  "Serializes a message object of type '<first_msg>"
  (cl:let ((__sec (cl:floor (cl:slot-value msg 'start_time)))
        (__nsec (cl:round (cl:* 1e9 (cl:- (cl:slot-value msg 'start_time) (cl:floor (cl:slot-value msg 'start_time)))))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __sec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 0) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __nsec) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __nsec) ostream))
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'msg_seq)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'msg_seq)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'original_num)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'original_num)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <first_msg>) istream)
  "Deserializes a message object of type '<first_msg>"
    (cl:let ((__sec 0) (__nsec 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __sec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 0) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __nsec) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __nsec) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'start_time) (cl:+ (cl:coerce __sec 'cl:double-float) (cl:/ __nsec 1e9))))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'msg_seq)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'msg_seq)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'original_num)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) (cl:slot-value msg 'original_num)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<first_msg>)))
  "Returns string type for a message object of type '<first_msg>"
  "custom_msg_pkg/first_msg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'first_msg)))
  "Returns string type for a message object of type 'first_msg"
  "custom_msg_pkg/first_msg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<first_msg>)))
  "Returns md5sum for a message object of type '<first_msg>"
  "4d5888a5a4bca89c6d6a476ac8a88a1a")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'first_msg)))
  "Returns md5sum for a message object of type 'first_msg"
  "4d5888a5a4bca89c6d6a476ac8a88a1a")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<first_msg>)))
  "Returns full string definition for message of type '<first_msg>"
  (cl:format cl:nil "time start_time~%uint16 msg_seq~%uint16 original_num~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'first_msg)))
  "Returns full string definition for message of type 'first_msg"
  (cl:format cl:nil "time start_time~%uint16 msg_seq~%uint16 original_num~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <first_msg>))
  (cl:+ 0
     8
     2
     2
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <first_msg>))
  "Converts a ROS message object to a list"
  (cl:list 'first_msg
    (cl:cons ':start_time (start_time msg))
    (cl:cons ':msg_seq (msg_seq msg))
    (cl:cons ':original_num (original_num msg))
))
