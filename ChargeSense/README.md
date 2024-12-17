---

## ChargeSense  

**ChargeSense** is a simple Python script that automatically shuts down your PC when it is unplugged from the charger. It ensures your battery life is conserved and prevents unauthorized use while on battery power.  

---

### Features  
- Monitors the laptop's power state.  
- Shuts down the system 30 seconds after detecting it is unplugged.  
- Resets automatically if the charger is reconnected.  

---

### Prerequisites  
1. Python 3.x  
2. `psutil` library (Install using `pip install psutil`)  

---

### Installation  
1. Clone this repository:  
   ```bash  
   git clone https://github.com/raviheima/LazyScripts.git  
   ```  
2. Navigate to the script folder:  
   ```bash  
   cd LazyScripts  
   ```  
3. Install required dependencies:  
   ```bash  
   pip install psutil  
   ```  

---

### Usage  
1. Run the script:  
   ```bash  
   python3 chargesense.py  
   ```  
2. The script will:  
   - Monitor if the charger is disconnected.  
   - Initiate shutdown after 30 seconds.  

---

### Notes  
- Works on Linux systems (`shutdown now` command).  
- Modify the shutdown command for other platforms (e.g., Windows).  
- Useful for battery conservation and preventing unauthorized use.  

---

### Author  
**Raviheima**  
[GitHub Profile](https://github.com/raviheima)  

---

### License  
This project is licensed under the MIT License.  

---  