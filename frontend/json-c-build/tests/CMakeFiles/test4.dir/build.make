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
CMAKE_SOURCE_DIR = "/home/omadbek/Desktop/Heal Star/frontend/json-c"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "/home/omadbek/Desktop/Heal Star/frontend/json-c-build"

# Include any dependencies generated for this target.
include tests/CMakeFiles/test4.dir/depend.make

# Include the progress variables for this target.
include tests/CMakeFiles/test4.dir/progress.make

# Include the compile flags for this target's objects.
include tests/CMakeFiles/test4.dir/flags.make

tests/CMakeFiles/test4.dir/test4.c.o: tests/CMakeFiles/test4.dir/flags.make
tests/CMakeFiles/test4.dir/test4.c.o: /home/omadbek/Desktop/Heal\ Star/frontend/json-c/tests/test4.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="/home/omadbek/Desktop/Heal Star/frontend/json-c-build/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building C object tests/CMakeFiles/test4.dir/test4.c.o"
	cd "/home/omadbek/Desktop/Heal Star/frontend/json-c-build/tests" && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/test4.dir/test4.c.o   -c "/home/omadbek/Desktop/Heal Star/frontend/json-c/tests/test4.c"

tests/CMakeFiles/test4.dir/test4.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/test4.dir/test4.c.i"
	cd "/home/omadbek/Desktop/Heal Star/frontend/json-c-build/tests" && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E "/home/omadbek/Desktop/Heal Star/frontend/json-c/tests/test4.c" > CMakeFiles/test4.dir/test4.c.i

tests/CMakeFiles/test4.dir/test4.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/test4.dir/test4.c.s"
	cd "/home/omadbek/Desktop/Heal Star/frontend/json-c-build/tests" && /usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S "/home/omadbek/Desktop/Heal Star/frontend/json-c/tests/test4.c" -o CMakeFiles/test4.dir/test4.c.s

# Object files for target test4
test4_OBJECTS = \
"CMakeFiles/test4.dir/test4.c.o"

# External object files for target test4
test4_EXTERNAL_OBJECTS =

tests/test4: tests/CMakeFiles/test4.dir/test4.c.o
tests/test4: tests/CMakeFiles/test4.dir/build.make
tests/test4: libjson-c.so.5.3.0
tests/test4: tests/CMakeFiles/test4.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir="/home/omadbek/Desktop/Heal Star/frontend/json-c-build/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable test4"
	cd "/home/omadbek/Desktop/Heal Star/frontend/json-c-build/tests" && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/test4.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
tests/CMakeFiles/test4.dir/build: tests/test4

.PHONY : tests/CMakeFiles/test4.dir/build

tests/CMakeFiles/test4.dir/clean:
	cd "/home/omadbek/Desktop/Heal Star/frontend/json-c-build/tests" && $(CMAKE_COMMAND) -P CMakeFiles/test4.dir/cmake_clean.cmake
.PHONY : tests/CMakeFiles/test4.dir/clean

tests/CMakeFiles/test4.dir/depend:
	cd "/home/omadbek/Desktop/Heal Star/frontend/json-c-build" && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" "/home/omadbek/Desktop/Heal Star/frontend/json-c" "/home/omadbek/Desktop/Heal Star/frontend/json-c/tests" "/home/omadbek/Desktop/Heal Star/frontend/json-c-build" "/home/omadbek/Desktop/Heal Star/frontend/json-c-build/tests" "/home/omadbek/Desktop/Heal Star/frontend/json-c-build/tests/CMakeFiles/test4.dir/DependInfo.cmake" --color=$(COLOR)
.PHONY : tests/CMakeFiles/test4.dir/depend

