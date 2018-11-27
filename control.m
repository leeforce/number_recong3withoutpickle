import java.awt.Robot;
import java.awt.event.*;
robot = java.awt.Robot;
forward = 120;
back = 600;
left = 600;
right = 600;
a = 0;
% while(a == 0)
%     time1 = datestr(now,'HH:MM:SS.FFF')
%     if time1 == '10:0:50.123'
%         a = 1;
%     end
% end

robot.mouseMove(750,400);
robot.mousePress(java.awt.event.InputEvent.BUTTON1_MASK);
pause(0.1)
robot.mouseRelease(java.awt.event.InputEvent.BUTTON1_MASK);
pause(1);
for i = 1:forward
    robot.keyPress(java.awt.event.KeyEvent.VK_W);
    robot.keyRelease(java.awt.event.KeyEvent.VK_W);
    pause(0.001);
end
pause(2)

for i = 1:back
    robot.keyPress(java.awt.event.KeyEvent.VK_S);
    robot.keyRelease(java.awt.event.KeyEvent.VK_S);
    pause(0.001);
end
for i = 1:left
    robot.keyPress(java.awt.event.KeyEvent.VK_A);
    robot.keyRelease(java.awt.event.KeyEvent.VK_A);
    pause(0.001);
end
pause(2)
for i = 1:right
    robot.keyPress(java.awt.event.KeyEvent.VK_D);
    robot.keyRelease(java.awt.event.KeyEvent.VK_D);
    pause(0.001);
end
pause(2)