# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/jong/Project4/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/jong/Project4/build

# Utility rule file for manager_generate_messages.

# Include the progress variables for this target.
include manager/CMakeFiles/manager_generate_messages.dir/progress.make

manager_generate_messages: manager/CMakeFiles/manager_generate_messages.dir/build.make

.PHONY : manager_generate_messages

# Rule to build all files generated by this target.
manager/CMakeFiles/manager_generate_messages.dir/build: manager_generate_messages

.PHONY : manager/CMakeFiles/manager_generate_messages.dir/build

manager/CMakeFiles/manager_generate_messages.dir/clean:
	cd /home/jong/Project4/build/manager && $(CMAKE_COMMAND) -P CMakeFiles/manager_generate_messages.dir/cmake_clean.cmake
.PHONY : manager/CMakeFiles/manager_generate_messages.dir/clean

manager/CMakeFiles/manager_generate_messages.dir/depend:
	cd /home/jong/Project4/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/jong/Project4/src /home/jong/Project4/src/manager /home/jong/Project4/build /home/jong/Project4/build/manager /home/jong/Project4/build/manager/CMakeFiles/manager_generate_messages.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : manager/CMakeFiles/manager_generate_messages.dir/depend

