
(cl:in-package :asdf)

(defsystem "custom_msg_pkg-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "first_msg" :depends-on ("_package_first_msg"))
    (:file "_package_first_msg" :depends-on ("_package"))
    (:file "second_msg" :depends-on ("_package_second_msg"))
    (:file "_package_second_msg" :depends-on ("_package"))
  ))