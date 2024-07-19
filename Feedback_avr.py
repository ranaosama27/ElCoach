class get_feedback_avr(object):

    def get_text(self, activity, score_list):

        text = ""
        # ---------------static tricep extension left------------------------
        if activity == "static_tricep_extension_left":
            r_flag = 0
            print("\n---------------------\n")
            print("score at 9\n")
            print(score_list[9])
            print("\n---------------------\n")
            print("\n---------------------\n")
            print("score at 7\n")
            print(score_list[7])
            print("\n---------------------\n")
            print("\n---------------------\n")
            print("score at 10\n")
            print(score_list[10])
            print("\n---------------------\n")
            print("\n---------------------\n")
            print("score at 8\n")
            print(score_list[8])
            print("\n---------------------\n")

            if score_list[9] not in range(55, 101) or score_list[7] not in range(60, 101):
                text += "\n Adjust your left Arm"
                r_flag = 1
            if score_list[10] not in range(45, 101) or score_list[8] not in range(49, 101):
                text += "\nAdjust your right Arm"
                r_flag = 1
            if r_flag == 1:
                text += "\nPlease try again and adjust your arms"
            else:
                text += "\nGood job"

        # ---------------static tricep extension right------------------------
        if activity == "static_tricep_extension_right":
            r_flag = 0
            print("\n---------------------\n")
            print("score at 9\n")
            print(score_list[9])
            print("\n---------------------\n")
            print("\n---------------------\n")
            print("score at 7\n")
            print(score_list[7])
            print("\n---------------------\n")
            print("\n---------------------\n")
            print("score at 10\n")
            print(score_list[10])
            print("\n---------------------\n")
            print("\n---------------------\n")
            print("score at 8\n")
            print(score_list[8])
            print("\n---------------------\n")

            if score_list[9] not in range(45, 101) or score_list[7] not in range(44, 101):
                text += "\n Adjust your left Arm"
                r_flag = 1
            if score_list[10] not in range(58, 101) or score_list[8] not in range(50, 101):
                text += "\nAdjust your right Arm"
                r_flag = 1
            if r_flag == 1:
                text += "\nPlease try again and adjust your arms"
            else:
                text += "\nGood job"
        # ---------------arm lifting ----------------------
        elif activity == "arm lifting":
            r_flag = 0
            if score_list[5] not in range(60, 101):
                text = " work out on your left shoulder"
                r_flag = 1
            if score_list[6] not in range(61, 101):
                text += "\n work out on your right shoulder"
                r_flag = 1
            if score_list[7] not in range(70, 101):
                text += "\n work out on your left elbow"
                r_flag = 1
            if score_list[8] not in range(60, 101):
                text += "\n work out on your right elbow"
                r_flag = 1
            if score_list[9] not in range(58, 101):
                text += "\n work out on your left wrist"
                r_flag = 1
            if score_list[10] not in range(41, 101):
                text += "\n work out on your right wrist"
                r_flag = 1
            if score_list[11] not in range(65, 101):
                text += "\n work out on your left hip"
                r_flag = 1
            if score_list[12] not in range(65, 101):
                text += "\n work out on your right hip"
                r_flag = 1
            if score_list[13] not in range(68, 101):
                text += "\n work out on your left knee"
                r_flag = 1
            if score_list[14] not in range(70, 101):
                text += "\n work out on your right knee"
                r_flag = 1
            if score_list[15] not in range(63, 101):
                text += "\n work out on your left ankle"
                r_flag = 1
            if score_list[16] not in range(61, 101):
                text += "\n work out on your right ankle"
                r_flag = 1

            if r_flag == 1:
                text += "\n Please try again "
            else:
                text += "\n Good job KEEP GOING"
        # ---------------shoulder abduction left ------------------------
        elif activity == "shoulder abduction":
            r_flag = 0
            if score_list[3] not in range(60, 101):
                text += "\nTry fixing your head"
                r_flag = 1
            if score_list[5] not in range(61, 101):
                text += "\nwork on your left shoulder"
                r_flag = 1
            if score_list[6] not in range(61, 101):
                text += "\nwork on your right shoulder"
                r_flag = 1
            if score_list[7] not in range(80, 101):
                text += "\nwork on your left elbow"
                r_flag = 1
            if score_list[8] not in range(65, 101):
                text += "\nwork on your right elbow"
                r_flag = 1
            if score_list[9] not in range(70, 101):
                text += "\nadjust your left wrist"
                r_flag = 1
            if score_list[10] not in range(65, 101):
                text += "\nadjust your right wrist"
                r_flag = 1
            if score_list[12] not in range(55, 101):
                text += "\ntry not to move your right leg"
                r_flag = 1
            if r_flag == 1:
                text += "\nPlease try again "
            else:
                text += "\nGood job KEEP GOING"
        # ---------------shoulder abduction right ------------------------
        elif activity == "shoulder abduction r":
            r_flag = 0
            if score_list[3] not in range(64, 101):
                print("Try fixing your head")
                r_flag = 1
            if score_list[5] not in range(70, 101):
                print("work on your left shoulder")
                r_flag = 1
            if score_list[6] not in range(69, 101):
                print("work on your right shoulder")
                r_flag = 1
            if score_list[7] not in range(75, 101):
                print("work on your left elbow")
                r_flag = 1
            if score_list[8] not in range(59, 101):
                print("work on your right elbow")
                r_flag = 1
            if score_list[9] not in range(69, 101):
                print("Adjust your left wrist")
                r_flag = 1
            if score_list[10] not in range(61, 101):
                print("Adjust your right wrist")
                r_flag = 1
            if score_list[11] not in range(76, 101):
                print("dont move your left leg")
                r_flag = 1
            if r_flag == 1:
                print("Please try again ")
            else:
                print("Good job KEEP GOING")

        # ---------------seated hamstring left ----------------------
        elif activity == "seated_hamstring_left":
            r_flag = 0
            if score_list[3] not in range(65, 101) or score_list[5] not in range(70, 101):
                text = " make your upper body straight with the chair"
                r_flag = 1
            if score_list[7] not in range(65, 101) or score_list[9] not in range(70, 101):
                text += "\n do not move your arm"
                r_flag = 1
            if score_list[11] not in range(62, 101):
                text += "\n dont move your left hip"
                r_flag = 1
            if score_list[13] not in range(50, 101):
                text += '\n work on your left knee'
                r_flag = 1
            if score_list[15] not in range(50, 101):
                text += "\n adjust you left ankle"
                r_flag = 1
            if r_flag == 1:
                text += "\n Please try again "
            else:
                text += "\n Good job KEEP GOING"

        # ---------------seated hamstring right ----------------------
        if activity == "seated_hamstring_right":
            r_flag = 0
            if score_list[4] not in range(59, 101) or score_list[6] not in range(48, 101):
                text = " make your upper body straight with the chair"
                r_flag = 1
            if score_list[8] not in range(52, 101) or score_list[10] not in range(64, 101):
                text += "\n do not move your arm"
                r_flag = 1
            if score_list[12] not in range(50, 101):
                text += "\n dont move your right hip"
                r_flag = 1
            if score_list[14] not in range(70, 101):
                text += '\n work on your right knee'
                r_flag = 1
            if score_list[16] not in range(60, 101):
                text += "\n straight your right ankle"
                r_flag = 1

            if r_flag == 1:
                print("Please try again ")
            else:
                print("Good job KEEP GOING")

                # ---------------circle arm right ----------------------
            if activity == "circle_arm_right":
                r_flag = 0
                if score_list[0] not in range(76, 101):
                    text = " make your upper body Down"
                    r_flag = 1
                if score_list[6] not in range(69, 101) or score_list[8] not in range(78, 101) or score_list[
                    10] not in range(78, 101):
                    text += "\n Make your right arm Straight and move it Circular motion"
                    r_flag = 1
                if score_list[5] not in range(63, 101) or score_list[7] not in range(79, 101) or score_list[
                    9] not in range(77, 101):
                    text += "\n dont move your left arm and hold the chair with rigth arm like L Latter"
                    r_flag = 1
                if r_flag == 1:
                    print("Please try again ")
                else:
                    print("Good job KEEP GOING")
                # ---------------circle arm left ----------------------
            if activity == "circle_arm_left":
                r_flag = 0
                if score_list[0] not in range(64, 101):
                    text = " make your upper body Down"
                    r_flag = 1
                if score_list[5] not in range(68, 101) or score_list[7] not in range(78, 101) or score_list[
                    9] not in range(68, 101):
                    text += "\n Make your left arm Straight and move it Circular motion"
                    r_flag = 1
                if score_list[6] not in range(66, 101) or score_list[8] not in range(76, 101) or score_list[
                    10] not in range(62, 101):
                    text += "\n dont move your right arm and hold the chair with rigth arm like L Latter"
                    r_flag = 1
                if r_flag == 1:
                    print("Please try again ")
                else:
                    print("Good job KEEP GOING")

                # ---------------swing arm left ----------------------
            if activity == "swing_arm_left":
                r_flag = 0
                if score_list[0] not in range(64, 101):
                    text = " make your upper body Down"
                    r_flag = 1
                if score_list[5] not in range(63, 101) or score_list[7] not in range(72, 101) or score_list[
                    9] not in range(66, 101):
                    text += "\n Make your left arm Straight and move it"
                    r_flag = 1
                if score_list[6] not in range(53, 101) or score_list[8] not in range(43, 101) or score_list[
                    10] not in range(7, 101):
                    text += "\n dont move your right arm and hold the chair with rigth arm like l Letter"
                    r_flag = 1
                if r_flag == 1:
                    print("Please try again ")
                else:
                    print("Good job KEEP GOING")

                # ---------------swing arm right ----------------------
            if activity == "swing_arm_right":
                r_flag = 0
                if score_list[0] not in range(61, 101):
                    text = " make your upper body Down"
                    r_flag = 1
                if score_list[6] not in range(63, 101) or score_list[8] not in range(53, 101) or score_list[10] not in range(47, 101):
                    text += "\n Make your right arm Straight and move it"
                    r_flag = 1
                if score_list[5] not in range(71, 101) or score_list[7] not in range(66, 101) or score_list[9] not in range(49, 101):
                    text += "\n dont move your left arm and hold the chair with left arm like l letter"
                    r_flag = 1
                if r_flag == 1:
                    print("Please try again ")
                else:
                    print("Good job KEEP GOING")


        # ---------------leg lifting extension right ----------------------
        elif activity == "seated_leg_lifting_right":
            r_flag = 0
            if score_list[0] not in range(65, 101):
                text += "\n dont move your head"
                r_flag = 1
            if score_list[5] not in range(75, 101) or score_list[6] not in range(49, 101):
                text = " dont move your shoulders"
                r_flag = 1
            if score_list[7] not in range(70, 101) or score_list[9] not in range(70, 101):
                text += "\n do not move your left arm, put it on your hip"
                r_flag = 1
            if score_list[8] not in range(49, 101) or score_list[10] not in range(51, 101):
                text += "\n do not move your right arm, put it on your hip"
                r_flag = 1
            if score_list[11] not in range(70, 101) or score_list[13] not in range(65, 101):
                text += '\n work on your left leg'
                r_flag = 1
            if score_list[12] not in range(55, 101) or score_list[14] not in range(55, 101):
                text += "\n fix your right leg next to your left leg"
                r_flag = 1

            if r_flag == 1:
                print("Please try again ")
            else:
                print("Good job KEEP GOING")
        # ---------------leg lifting extension left ----------------------
        elif activity == "seated_leg_lifting_left":
            r_flag = 0
            if score_list[0] not in range(55, 101):
                text += "\n dont move your head"
                r_flag = 1
            if score_list[5] not in range(73, 101) or score_list[6] not in range(55, 101):
                text = " dont move your shoulders"
                r_flag = 1
            if score_list[7] not in range(66, 101) or score_list[9] not in range(65, 101):
                text += "\n do not move your left arm, put it on your hip"
                r_flag = 1
            if score_list[8] not in range(51, 101) or score_list[10] not in range(51, 101):
                text += "\n do not move your right arm, put it on your hip"
                r_flag = 1
            if score_list[11] not in range(65, 101) or score_list[13] not in range(61, 101):
                text += '\n fix your left leg next to your right leg'
                r_flag = 1
            if score_list[12] not in range(56, 101) or score_list[14] not in range(49, 101):
                text += "\n work on your right leg"
                r_flag = 1

            if r_flag == 1:
                print("Please try again ")
            else:
                print("Good job KEEP GOING")


        return text
