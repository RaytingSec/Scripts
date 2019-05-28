#!/bin/bash
# Bug with some intel chipsets where USB 3.0 wakeup can't be disabled. Have to manually disable each boot.

echo "XHCI" | sudo tee /proc/acpi/wakeup
sleep 0.25
echo "IGBE" | sudo tee /proc/acpi/wakeup
sleep 0.25
echo "SLPB" | sudo tee /proc/acpi/wakeup
