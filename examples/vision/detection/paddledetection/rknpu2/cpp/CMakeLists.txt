CMAKE_MINIMUM_REQUIRED(VERSION 3.10)
project(rknpu2_test)

set(CMAKE_CXX_STANDARD 14)

# 指定下载解压后的fastdeploy库路径
set(FASTDEPLOY_INSTALL_DIR "thirdpartys/fastdeploy-0.0.3")

include(${FASTDEPLOY_INSTALL_DIR}/FastDeployConfig.cmake)
include_directories(${FastDeploy_INCLUDE_DIRS})

add_executable(infer_picodet infer_picodet.cc)
target_link_libraries(infer_picodet ${FastDeploy_LIBS})



set(CMAKE_INSTALL_PREFIX ${CMAKE_SOURCE_DIR}/build/install)

install(TARGETS infer_picodet DESTINATION ./)

install(DIRECTORY model DESTINATION ./)
install(DIRECTORY images DESTINATION ./)

file(GLOB FASTDEPLOY_LIBS ${FASTDEPLOY_INSTALL_DIR}/lib/*)
message("${FASTDEPLOY_LIBS}")
install(PROGRAMS ${FASTDEPLOY_LIBS} DESTINATION lib)

file(GLOB ONNXRUNTIME_LIBS ${FASTDEPLOY_INSTALL_DIR}/third_libs/install/onnxruntime/lib/*)
install(PROGRAMS ${ONNXRUNTIME_LIBS} DESTINATION lib)

install(DIRECTORY ${FASTDEPLOY_INSTALL_DIR}/third_libs/install/opencv/lib DESTINATION ./)

file(GLOB PADDLETOONNX_LIBS ${FASTDEPLOY_INSTALL_DIR}/third_libs/install/paddle2onnx/lib/*)
install(PROGRAMS ${PADDLETOONNX_LIBS} DESTINATION lib)

file(GLOB RKNPU2_LIBS ${FASTDEPLOY_INSTALL_DIR}/third_libs/install/rknpu2_runtime/${RKNN2_TARGET_SOC}/lib/*)
install(PROGRAMS ${RKNPU2_LIBS} DESTINATION lib)
