# StopLightSim.py
# Name: Mia Garcia
# Date: 4/23/26
# Assignment: Lab 11

import simpy


greenLight = True


def stopLight(env):
    """Simulates a traffic light that cycles between green, yellow, and red."""
    global greenLight

    while True:
        print("Green at time", env.now)
        greenLight = True
        yield env.timeout(30)

        print("Yellow at time", env.now)
        yield env.timeout(2)

        print("Red at time", env.now)
        greenLight = False
        yield env.timeout(20)


def car(env, car_id):

    print("Car", car_id, "arrived at", env.now)

    global greenLight

    while not greenLight:
        print("Car", car_id, "waiting at", env.now)
        yield env.timeout(1)

    print("Car", car_id, "departed at", env.now)


def carArrival(env):

    car_id = 0

    while True:
        car_id += 1
        print("Creating Car", car_id)

        env.process(car(env, car_id))

        yield env.timeout(5)


def main():
    env = simpy.Environment()

    env.process(stopLight(env))

    env.process(carArrival(env))

    env.run(until=100)

    print("Simulation complete")


if __name__ == "__main__":
    main()