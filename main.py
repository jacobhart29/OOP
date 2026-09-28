class Sensor:
    def __init__(self, sensor_type: str, status: str = "Active"):
        self.sensor_type = sensor_type
        self.status = status

    def get_data(self) -> str:
        return f"{self.sensor_type} Sensor [{self.status}]"

class Robot:
    VALID_STATUSES = {"Active", "Online", "Offline", "Idle"}

    def __init__(self, robot_id: int, name: str, battery_level: float, status: str = "Idle"):
        self.robot_id = robot_id
        self._name = name
        self._battery_level = 0.0
        self._status = "Idle"

        self.battery_level = battery_level
        self.status = status

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

class RobotCar(Robot):
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

class RobotArm(Robot):
    def __init__(self, robot_id: int, name: str, battery_level: float, payload_weight: float, status: str = "Idle"):
        super().__init__(robot_id, name, battery_level, status)
        self.payload_weight = payload_weight

    @property
    def payload_weight(self) -> float:
        return self._payload_weight

    @payload_weight.setter
    def payload_weight(self, weight: float):
        if not isinstance(weight, (int, float)) or weight < 0:
            raise ValueError("Payload weight must be a non-negative number.")
        self._payload_weight = float(weight)

if __name__ == "__main__":
    robot = Robot(robot_id=101, name="JKF", battery_level=90, status="Online")
    robot_car = RobotCar(robot_id=100, name="RFK", battery_level=50, speed=10, max_speed=50, status="Offline")
    robot_arm = RobotArm(robot_id=102, name="ARM-1", battery_level=80, payload_weight=15.5, status="Idle")

    print(robot.get_info())
    print(f"Car Speed: {robot_car.speed}")
    print(f"Arm Payload: {robot_arm.payload_weight} kg")

    try:
        robot_car.speed = 60
    except ValueError as err:
        print(f"Validation caught error: {err}")

    try:
        robot_arm.payload_weight = -5
    except ValueError as err:
        print(f"Validation caught error: {err}")