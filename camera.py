from picamera2 import Picamera2 # pip install picamera2
import subprocess
from flask import jsonify
def plant_picture():
    picam2 = Picamera2()
    camera_config = picam2.create_preview_configuration()
    picam2.configure(camera_config)
    picam2.start()
    # /home/pi/CUCU_FE/COUQUE-DASSE-FRONT/front/public/myPlnat
    # /home/pi/imgs/
    p = subprocess.check_output("cd /home/pi/CUCU_FE/COUQUE-DASSE-FRONT/front/public/myPlnat/; ls -l | grep ^- | wc -l; cd ../..",shell=True, encoding='utf-8')
    p =str(p)
    p = p[:len(p)-1]
    print(p)
    # picam2.capture_file(f"../imgs/pic{p}.jpg")
    picam2.capture_file(f"/home/pi/CUCU_FE/COUQUE-DASSE-FRONT/front/public/myPlnat/pic{p}.jpg")
    # pic_path = f"/home/pi/imgs/pic{p}.jpg"
    pic_path = f"./myPlnat/pic{p}.jpg"
    picam2.close()
    return str(pic_path)
    # return jsonify({'path':pic_path}) # ./static/imgs/pic{p}.jpg #, p