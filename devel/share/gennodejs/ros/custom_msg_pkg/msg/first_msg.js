// Auto-generated. Do not edit!

// (in-package custom_msg_pkg.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class first_msg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.start_time = null;
      this.msg_seq = null;
      this.original_num = null;
    }
    else {
      if (initObj.hasOwnProperty('start_time')) {
        this.start_time = initObj.start_time
      }
      else {
        this.start_time = {secs: 0, nsecs: 0};
      }
      if (initObj.hasOwnProperty('msg_seq')) {
        this.msg_seq = initObj.msg_seq
      }
      else {
        this.msg_seq = 0;
      }
      if (initObj.hasOwnProperty('original_num')) {
        this.original_num = initObj.original_num
      }
      else {
        this.original_num = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type first_msg
    // Serialize message field [start_time]
    bufferOffset = _serializer.time(obj.start_time, buffer, bufferOffset);
    // Serialize message field [msg_seq]
    bufferOffset = _serializer.uint16(obj.msg_seq, buffer, bufferOffset);
    // Serialize message field [original_num]
    bufferOffset = _serializer.uint16(obj.original_num, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type first_msg
    let len;
    let data = new first_msg(null);
    // Deserialize message field [start_time]
    data.start_time = _deserializer.time(buffer, bufferOffset);
    // Deserialize message field [msg_seq]
    data.msg_seq = _deserializer.uint16(buffer, bufferOffset);
    // Deserialize message field [original_num]
    data.original_num = _deserializer.uint16(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 12;
  }

  static datatype() {
    // Returns string type for a message object
    return 'custom_msg_pkg/first_msg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '4d5888a5a4bca89c6d6a476ac8a88a1a';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    time start_time
    uint16 msg_seq
    uint16 original_num
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new first_msg(null);
    if (msg.start_time !== undefined) {
      resolved.start_time = msg.start_time;
    }
    else {
      resolved.start_time = {secs: 0, nsecs: 0}
    }

    if (msg.msg_seq !== undefined) {
      resolved.msg_seq = msg.msg_seq;
    }
    else {
      resolved.msg_seq = 0
    }

    if (msg.original_num !== undefined) {
      resolved.original_num = msg.original_num;
    }
    else {
      resolved.original_num = 0
    }

    return resolved;
    }
};

module.exports = first_msg;
