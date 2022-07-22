<!-- ---------------------------------------------------------------------- -->

---
# THE SUPER HYPER POKE DIGI MEGA MUCHI-FANTASTIC FINAL PROJECT (2D-BASIC-PLANNER)
NAME: Juan Camilo Torres Mestra
---
## SOLUTION TO QUESTIONARY AND REPORT
https://drive.google.com/drive/folders/1qigeC1ViWLvBXHuX1ZNrfbyfYZYQwJN0?usp=sharing
---
## INSTRUCTIONS:
1. Fork this repository, and associate it with your GitHub account.
2. Create a new branch name as `develop` and work all your solutions there.
3. Every time that you complete a basic point create a commit, add the files and push with the next format description: `[FEAT]: description of what you did`.
4. You can do your last commit and push until and before the deadline (date & time) if you do more after, we will make a reverse of your code until the last commit before the dead-line date&time (If the project is not complete there, it'll be rejected).
5. Remember partial solutions will be no accepted, you have to complete at least **BASIC POINTS**, **QUESTIONARY**, but we consider the real project the **EXTRA-HOMEWORK** session (Without it your chances will be less).

--------
**BASIC POINTS**:

Here are the basic points to accomplish the project, what we are evaluating you is the knowledge in python, GCP API's,  ROS2 in a basic level of concepts and implementation. This part of the project is more for the understanding of itself because we invite you to make the extra-homework, which is the real challenge, where you'll have to be more creative and go further. 

Well, the recommendation in this section is to start with the python nodes. You won't have to change the input or output attributes in any function or method, just implement functions contents, and operations, import a library and use it inside. 

Try first to understand the function of the node in the whole stack, then what is every function for, read the documentation and docs provided, and look for the TODO sections in these.

If you follow the instruction to launch all the stack you'll get a window like this:

<p align="center">
  <img height="300" src="https://user-images.githubusercontent.com/43115782/116264723-27a80380-a740-11eb-8e03-62039517b82a.png">
</p>

running the stack from the root, remember the command is:

        ada@vision1050:/workspace$ bash planner/configs/startPlanner.sh start

If you can not get this window it could be that the code you are making is broken, you are having packages building errors, or having the xhost display error. But before starting to code you solution make sure that you have this window.

### *Python*

If you complete python points you'll have the robot moving in the map.

1. **Implement/Create the path planner status subscriber** - package: [`graphics`](https://github.com/kiwicampus/2D-Test-Track-Service-Desk-Project/tree/main/planner/ROS2/src/graphics), Node: [`node_visual_gui.py`](https://github.com/kiwicampus/2D-Test-Track-Service-Desk-Project/tree/main/planner/ROS2/src/graphics/graphics/node_visual_gui.py) -> Implement/Create in the node constructor a subscriber for the bot status, the topic name should be `/path_planner/msg` message type `planner_msg`, callback `cb_path_planner`.

2. **Implement/Create the Kiwibot status subscriber** - package: [`graphics`](https://github.com/kiwicampus/2D-Test-Track-Service-Desk-Project/tree/main/planner/ROS2/src/graphics), Node: [`node_visual_gui.py`](https://github.com/kiwicampus/2D-Test-Track-Service-Desk-Project/tree/main/planner/ROS2/src/graphics/graphics/node_visual_gui.py) -> Implement/Create in the node constructor a subscriber for the bot status, the topic name should be `/kiwibot/status` message type `kiwibot_msg`, callback `cb_kiwibot_status`.

3. **Drawing map descriptors** - package: [`graphics`](https://github.com/kiwicampus/2D-Test-Track-Service-Desk-Project/tree/main/tree/main/planner/ROS2/src/graphics), Node: [`node_visual_gui.py`](https://github.com/kiwicampus/2D-Test-Track-Service-Desk-Project/tree/main/planner/tree/main/ROS2/src/graphics/graphics/node_visual_gui.py) -> Implement the function `draw_descriptors` to draw every landmark in the map when a routine is loaded, please base on the red circles in the video example. **Note**: Do not add extra attributes o return.

4. **Draw the robot** - package: [`graphics`](https://github.com/kiwicampus/2D-Test-Track-Service-Desk-Project/tree/main/tree/main/planner/ROS2/src/graphics), Node: [`node_visual_gui.py`](https://github.com/kiwicampus/2D-Test-Track-Service-Desk-Project/tree/main/tree/main/planner/ROS2/src/graphics/graphics/node_visual_gui.py) -> Implement the function `draw_robot` to draw the robot over the map, you can use the function `overlay_image` located in the utils module in the `python_utils.py` file. **Note**: Do not add extra attributes o return.

If you finish successfully all the points, you must have a window like this (with sounds included): 

 <p align="center">
     <img src="https://user-images.githubusercontent.com/43115782/114318886-99dbdf80-9ad4-11eb-947a-e7c6e417fec2.gif" alt="test_Track_map" width="300"/> 
</p>

### *Information Management* 

For the second part of the basics we want to assess the use of API's and information management, as well as written communication, problem solving, reporting skills and learn new technologies quickly and effectively, you can make use of online tutorials to guide you, anyway you will be doing it while you work with us :)

In this part you will need to install new libraries or dependencies. Be careful, there are many ways you could install a simple package, but we hope you do it in an elegant and containerized way.

1. **Generate [GCP](https://cloud.google.com/) credentials:** If you don't have an account generate one. You don't need to have billing activated, it will only be used in a basic way. The credentials can be saved anywhere you want (BE CAREFUL, DO NOT COMMIT OR PUSH YOUR CREDENTIALS).

2. **Authenticate credentials:** You must analyze the stack and decide in which scripts you must authenticate the credentials to be able to use the API later, keep in mind that the place you choose is because you want to get/upload information to google sheets. We use the following library: https://google-auth.readthedocs.io/en/master/

3. **Upload information to google sheet:** You must add a piece of code where you think it should go (be careful not to break anything), this code must add a new line in a google sheet every time a routine is started, the following information must be loaded: 

```id (different than routine_id), date, time, routine_id, total_distance, total_time ```

We use the following library: https://docs.gspread.org/en/latest/

4. **Make a report:** You should make a report explaining briefly what you did, the resources you used and all the necessary information you think we need to verify the result. It should not be a line by line explanation of what you did, just a description of the result, what you used and how we can access the information you saved. You can use any means and in the most assertive way to show it, just keep in mind that you must provide us with a way to see it for us.

---
**REMEMBER**: 
1. Once more again, No partial solution will be accepted, you have to complete all the basic points and the questionary to submit your solution to a review.
2. if you push just one minute after the time given by email we won't review your project solution (at least, that commit).
3. if you find an error in the code, bug, drawback, and there's no already an issue created in the main repository, please create it and you win extra points (+3%/5: **this is 3% more over 5.0, which is equal to 0.15 in the final project's grade**), we'll try to give a solution ASAP.
4. You have 5 questions that can be done as an issue in the main repository, so please check that what you are asking for is not already answered in the issues section (don't waste your questions).
5. It's forbidden talk with other project participants, if we think that you made tramp or you cheated, your project and the others (if apply) won't be reviewed and your application will be canceled.
6. We'll push the solution when the application job closes, we'll notify all participants of this by email.
7. What we are evaluating is:
    * **[5%/5]** Code style
    * **[5%/5]** Code Documentation
    * **[15%/5]** Questionary
    * **[25%/5]** Solution to basic home-work
    * **[50%/5]** Sustentation of your solution & answers
8. You can have a grade higher than 5.0.
9. We'll share the final grades with every candidate by email, with feedback included of his/her application (things to improve, to keep, to remove). The application process percentages are:
    * **[30%/5]** Cultural feed Interview
    * **[30%/5]** Pair programming Interview
    * **[40%/5]** Final Project
10. We are evaluating your concepts and knowledge in ROS2, Python, API's, Some basic control concepts, other Code stuff.
11. If no participant send the project before the dead line time, we will extend the deadline date and time, for everyone, with just person that complete the questionary and the basic-points the rest are doomed, but also if we considered that the solutions received are not enough or not well explained we also can extend the deadline, but we are pretty sure that this wont happened.

---
<!-- ---------------------------------------------------------------------- -->
## **QUESTIONARY**

Respond below every questions:

1. [Python] Why the robot's image gets distorted when is turning?

2. [Python] Are Python packages compiled as C++ packages?

3. [Python] Why with some code errors in some nodes the logs are not printed?

4. [Python] Why there are variables that begin with _?

5. [Python] Why do you put _ after the variable cols in this line?
    ```
    rows, cols, _ = self._kiwibot_img.shape
    ```
6. [API's] What would happen if we try to update the google sheet table every new execution frame?

7. [Docker] Explain with your own words what is the instructions `apt-get autoremove && apt-get clean -y for?`

8. [Docker] If you modify a layer what happen with the previous and the next ones?

9. [Docker] Can we change the basic image (`FROM ubuntu:20.04`) from the docker file to another?

10. [General] Why is it not a good idea to upload the API credentials to github and why if they are already uploaded is it not a good idea to simply delete them from your repo?


Next questions is after you finish the project, it doesn't give points but we really appreciate you feedback:
* What do you think about this project? is it hard or enough? is it to complicated, is it well structure, explanations and instructions are clear?

---
<!-- ---------------------------------------------------------------------- -->
## **EXTRA-HOMEWORK**

For extra homework we recommend you create a new branch from the developed one when you finish the basic points of the homework, you can name this new branch as *feature/extra_homework*, don't forget to push it before the time that it was given. For this you can create new files, modules and organize them as you wish.

1. **[+5%/5.0]**: Modify the docker file to source ROS2 and have autocompleted commands like ```ros2 topic list```.
2. **[+5%/5.0]**: Make that the Kiwibot image doesn't get distorted when is turning.
3. **[+10%/5.0]**: In the GUI, there's an empty field with the `Porc:???%` value. Find a way to print there the % of the total distance of the routine that the robot has traveled.
<img height="300" src="https://user-images.githubusercontent.com/38380745/143324697-a06fb3ae-de62-4d42-8373-0da62e68a314.png">

4. **[+10%/5.0]**: Implement a method or way to stop the routine (with a key).

5. **[+10%/5.0]**: Have the full data downloaded from the gsheet and saved in a .csv file each time the container is opened.

6. **[+20%/5.0]**: Update the data from the gsheet every time the routine is paused or the robot reach a waypoint with the percent data form the point 4 (create a new column for this field). You must update the row of the current routine, not create a new row.

7. **[+15%/5.0]:** Here you could add a new "completed" column, and define it as 1 -> completed routines or 0 -> uncompleted routines.

8. **[+10%/5.0]**: Filter the information in the google sheet table by routine and generate a chart with the total distance traveled.

9. **[+10%/5.0]**: Add the previous chart the option to show the completed and uncompleted routines.

10. **[+5%/5.0]**: (Question) What happens if we change some element of the google sheets sheet for example: file name, time name, sheet position, etc?

Total possible Extra points: 100% -> 5.0. Maximum total grade: 10.0/5.0. Complete the point it doesn't mean you have 5.0, you have at least 3.0 but for the rest of the grade will evaluate the performance and the beauty of your solution. To complete these points, probably you will have to modify messages, services, or even create new ones, also topics subscribers and publishers, maybe services, who knows :)

---
Good luck, and God saves the Queen.

<p align="center">
  <img height="300" src="https://media.tenor.com/images/18a922837758f4d77b983dfa1f7acff2/tenor.gif">
</p>


*Davidson DO NOT forget erase the [solution branch](https://www.youtube.com/watch?v=dQw4w9WgXcQ)*
