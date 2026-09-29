"""all the code i wrote"""

running = True
robots = []

class Sensor:
    """
    Handles the sensor data for robots.
    """
    def __init__(self, sensor_type: str, status: str = "Active"):
        self.sensor_type = sensor_type
        self.status = status

    def get_data(self) -> str:
        return f"{self.sensor_type} Sensor [{self.status}]"
    # data 

class Robot:
    """
    Base class for all of the robot types.
    """
    VALID_STATUSES = {"Active", "Online", "Offline", "Idle"}

    robots: list['Robot'] = []

    def __init__(self, robot_id: int, name: str, battery_level: float, status: str = "Idle"):
        self.robot_id = robot_id
        self._name = name
        self._battery_level = 0.0
        self._status = "Idle"

        self.battery_level = battery_level
        self.status = status

        self.sensors: list[Sensor] = []
        Robot.robots.append(self)

    def add_sensor(self, sensor: Sensor):
        if isinstance(sensor, Sensor):
            self.sensors.append(sensor)
            print(f"[{self._name}] Attached {sensor.sensor_type} Sensor.")
        else:
            raise TypeError("Only valid Sensor instances can be added.")
        
    def check_sensors(self) -> str:
        if not self.sensors:
            return f"[{self._name}] No sensors attached."
        
        sensor_reports = [sensor.get_data() for sensor in self.sensors]
        return f"[{self._name}] Sensors: {', '.join(sensor_reports)}"

    @property
    def battery_level(self) -> float:
        return self._battery_level

    @battery_level.setter
    def battery_level(self, value: float):
        if not isinstance(value, (int, float)) or not (0 <= value <= 100):
            raise ValueError("Battery level must be a number between 0 and 100.")
        self._battery_level = float(value)

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, value: str):
        formatted_value = value.capitalize() if value else ""
        if formatted_value not in self.VALID_STATUSES:
            raise ValueError(f"Status must be one of: {', '.join(self.VALID_STATUSES)}")
        self._status = formatted_value

    def get_info(self) -> str:
        return f"{self.robot_id} | Name: {self._name} | Battery: {self.battery_level}% | Status: {self.status}"

    def charge(self, amount: float):
        new_level = self.battery_level + amount
        self.battery_level = min(100.0, new_level)
        print(f"[{self._name}] Charged to {self.battery_level}%.")

    def reset_status(self):
        self.status = "Idle"
        print(f"[{self._name}] Status reset to Idle.")

    def __str__(self) -> str:
        return f"Robot ID: {self.robot_id}, Name: {self._name}, Battery: {self.battery_level}%, Status: {self.status}"

class RobotCar(Robot):
    """
    Handles all of the robot car functions like speed and max speed and inherits from the Robot class.
    """
    VALID_STATUSES = {"Driving", "Online", "Offline", "Idle", "Crashed"}

    def __init__(self, robot_id: int, name: str, battery_level: float, speed: float, max_speed: float, status: str = "Idle"):
        super().__init__(robot_id, name, battery_level, status)
        self._max_speed = max_speed
        self.speed = speed 

    @property
    def speed(self) -> float:
        return self._speed

    @speed.setter
    def speed(self, speed: float):
        if not isinstance(speed, (int, float)) or not (0 <= speed <= self._max_speed):
            raise ValueError(f"Speed must be a number between 0 and {self._max_speed}")
        self._speed = float(speed)

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, value: str):
        formatted_value = value.capitalize() if value else ""
        if formatted_value not in self.VALID_STATUSES:
            raise ValueError(f"Status must be one of: {', '.join(self.VALID_STATUSES)}")
        self._status = formatted_value

    def charge(self, amount: float):
        new_level = self.battery_level + amount
        self.battery_level = min(100.0, new_level)
        print(f"ROBOT CAR [{self._name}] Charged to {self.battery_level}%.")

class RobotArm(Robot):
    """
    Handles all of the robot arm functions like payload and weight and removes the charge functions and inherits from the Robot class.
    """
    def __init__(self, robot_id: int, name: str, battery_level: float, payload_weight: float, status: str = "Idle"):
        super().__init__(robot_id, name, battery_level, status)
        self.payload_weight = payload_weight

    @property
    def payload_weight(self) -> float:
        # this is cuz robot arm is bad
        return self._payload_weight

    @payload_weight.setter
    def payload_weight(self, weight: float):
        if not isinstance(weight, (int, float)) or weight < 0:
            raise ValueError("Payload weight must be a non-negative number.")
        self._payload_weight = float(weight)

    def charge(self, amount: float):
        # no battery mean no charge
        print(f"ROBOT ARM DOES NOT HAVE BATTERY")

def find_robot_by_id(robots: list[Robot]) -> Robot:
    """
    Docstring for find_robot_by_id
    
    :param robots: Description
    :type robots: list[Robot]
    :return: Description
    :rtype: Robot
    """
    try:
        target_id = int(input("Enter target Robot ID: "))
    except ValueError:
        raise ValueError("Robot ID must be an integer.")

    for robot in robots:
        if robot.robot_id == target_id:
            return robot

    raise KeyError(f"No robot found with ID {target_id}.")

def main():
    """
    Handles all of the user input and commands for the robots. and creates the robots and adds them to the list of robots.
    """
    global running
    running = True

    Robot(robot_id=101, name="JKF", battery_level=90, status="Online")
    RobotCar(robot_id=100,name="RFK",battery_level=50,speed=10,max_speed=50,status="Offline",)
    RobotArm(robot_id=102,name="ARM-1",battery_level=80,payload_weight=15.5,status="Idle",)

    while running:
        user_input = (input("\nEnter command (view, check_sensors, charge, reset_status, add_sensor, exit): ").strip().lower())

        if user_input == "exit":
            print("Exiting loop...")
            running = False

        elif user_input == "view":
            for r in Robot.robots:
                print(r.get_info())

        elif user_input == "check_sensors":
            for r in Robot.robots:
                print(r.check_sensors())

        elif user_input == "charge":
            try:
                target = find_robot_by_id(Robot.robots)
                amount = float(input("Enter charge amount: "))
                target.charge(amount)
            except (ValueError, KeyError) as err:
                print(f"[ERROR] {err}")

        elif user_input == "reset_status":
            try:
                target = find_robot_by_id(Robot.robots)
                target.reset_status()
            except (ValueError, KeyError) as err:
                print(f"[ERROR] {err}")

        elif user_input == "add_sensor":
            try:
                target = find_robot_by_id(Robot.robots)
                sensor_type = input("Enter sensor type: ").strip()
                if not sensor_type:
                    raise ValueError("Sensor type cannot be empty.")
                target.add_sensor(Sensor(sensor_type))
            except (ValueError, KeyError, TypeError) as err:
                print(f"[ERROR] {err}")

        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()