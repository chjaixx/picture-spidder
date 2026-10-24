/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 80043
 Source Host           : localhost:3306
 Source Schema         : students1

 Target Server Type    : MySQL
 Target Server Version : 80043
 File Encoding         : 65001

 Date: 24/10/2026 16:12:01
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for class_shedule
-- ----------------------------
DROP TABLE IF EXISTS `class_shedule`;
CREATE TABLE `class_shedule`  (
  `课程编号` int NOT NULL,
  `课程名称` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`课程编号`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of class_shedule
-- ----------------------------
INSERT INTO `class_shedule` VALUES (1011, '外语');
INSERT INTO `class_shedule` VALUES (1102, '数学');
INSERT INTO `class_shedule` VALUES (1103, '体育');
INSERT INTO `class_shedule` VALUES (1104, '历史');
INSERT INTO `class_shedule` VALUES (1105, 'MySQL');
INSERT INTO `class_shedule` VALUES (1106, 'python');

-- ----------------------------
-- Table structure for grade
-- ----------------------------
DROP TABLE IF EXISTS `grade`;
CREATE TABLE `grade`  (
  `学号` int NULL DEFAULT NULL,
  `姓名` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `课程编号` int NULL DEFAULT NULL,
  `课程名称` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `成绩` decimal(5, 2) NULL DEFAULT NULL,
  INDEX `gra_fk`(`学号` ASC) USING BTREE,
  INDEX `graa_fk`(`课程编号` ASC) USING BTREE,
  CONSTRAINT `gra_fk` FOREIGN KEY (`学号`) REFERENCES `student` (`学号`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `graa_fk` FOREIGN KEY (`课程编号`) REFERENCES `class_shedule` (`课程编号`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of grade
-- ----------------------------
INSERT INTO `grade` VALUES (2401, '王东', 1011, '外语', 78.22);
INSERT INTO `grade` VALUES (2404, '梨花', 1104, 'MySQL', 77.60);

-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student`  (
  `学号` int NOT NULL,
  `姓名` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `班级` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`学号`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of student
-- ----------------------------
INSERT INTO `student` VALUES (2401, '王东', '一班');
INSERT INTO `student` VALUES (2402, '李化', '一班');
INSERT INTO `student` VALUES (2403, '张三', '一班');
INSERT INTO `student` VALUES (2404, '梨花', '二班');

SET FOREIGN_KEY_CHECKS = 1;
