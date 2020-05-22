# Automated Routine

Shell scripts to simplify linux processes

## Installation

```
git clone https://github.com/armendgashi/automated-routine
```

## Usage

### GETIP

Shell script that prints out only the IP of your chosen Network Interface and copies it on your clipboard

```
chmod a+x getip.sh
./getip.sh interface
```

## Example

```
./getip.sh wlan0

OR you can use it as a binary

cp getip.sh /usr/bin/getip
getip wlan0
```