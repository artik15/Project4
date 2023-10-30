
(cl:in-package :asdf)

(defsystem "manager-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "SpeedControl" :depends-on ("_package_SpeedControl"))
    (:file "_package_SpeedControl" :depends-on ("_package"))
    (:file "SteeringControl" :depends-on ("_package_SteeringControl"))
    (:file "_package_SteeringControl" :depends-on ("_package"))
    (:file "manager" :depends-on ("_package_manager"))
    (:file "_package_manager" :depends-on ("_package"))
  ))