//
//  ViewController.swift
//  transitions mental health assoc
//
//  Created by Finlay Piroth on 1/7/20.
//  Copyright © 2020 Hack4Impact. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    //must scrape data from website to input into the table cells
    //CELLS -> text info, image
    //give buttons functionality
    
    //MARK: properties
    @IBOutlet weak var dashboardButton: UIButton!
    @IBOutlet weak var messagesButton: UIButton!
    @IBOutlet weak var patientDataButton: UIButton!
    
    @IBOutlet weak var dashboardContainerView: UIView!
    @IBOutlet weak var messagesContainerView: UIView!
    @IBOutlet weak var patientDataContainerView: UIView!
    
    var currentButton = 1
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        //set up buttons
        setButton(button: dashboardButton)
        dashboardButton.tag = 1
        dashboardButton.isSelected = true
        dashboardButton.backgroundColor = UIColor(red: 0.2588, green: 0.66667, blue: 0.8745, alpha: 1)
        setButton(button: messagesButton)
        messagesButton.tag = 2
        messagesButton.isSelected = false
        setButton(button: patientDataButton)
        patientDataButton.tag = 3
        patientDataButton.isSelected = false
        
        let tap: UITapGestureRecognizer = UITapGestureRecognizer(target: self, action: #selector(UIInputViewController.dismissKeyboard))
        
        view.addGestureRecognizer(tap)
        
        //init which view shown
        dashboardContainerView.alpha = 1
        messagesContainerView.alpha = 0
        patientDataContainerView.alpha = 0
    }

    
    //MARK: functions
    //switch between child container views with button presses
    @IBAction func navButtonPressed(_ sender: UIButton) {
        if sender.tag == 1 {
            if currentButton == 1 {
                return
            } else {
                UIView.animate(withDuration: 0.3, animations: {self.dashboardContainerView.alpha = 1; self.messagesContainerView.alpha = 0; self.patientDataContainerView.alpha = 0})
                dashboardButton.isSelected = true
                UIButton.animate(withDuration: 0.3, animations: {self.dashboardButton.backgroundColor = UIColor(red: 0.2588, green: 0.66667, blue: 0.8745, alpha: 1)})
                let curButton = self.view.viewWithTag(currentButton) as! UIButton
                UIButton.animate(withDuration: 0.3, animations:{ curButton.backgroundColor = UIColor(red: 0.443, green: 0.7843, blue: 0.8941, alpha: 1)})
                currentButton = 1
            }
        } else if sender.tag == 2 {
            if currentButton == 2 {
                return
            } else {
                UIView.animate(withDuration: 0.3, animations: {self.dashboardContainerView.alpha = 0; self.messagesContainerView.alpha = 1; self.patientDataContainerView.alpha = 0})
                messagesButton.isSelected = true
                UIButton.animate(withDuration: 0.3, animations: {self.messagesButton.backgroundColor = UIColor(red: 0.2588, green: 0.66667, blue: 0.8745, alpha: 1)})
                let curButton = self.view.viewWithTag(currentButton) as! UIButton
                UIButton.animate(withDuration: 0.3, animations:{ curButton.backgroundColor = UIColor(red: 0.443, green: 0.7843, blue: 0.8941, alpha: 1)})
                currentButton = 2
            }
        } else if sender.tag == 3 {
            if currentButton == 3 {
                return
            } else {
                UIView.animate(withDuration: 0.3, animations: {self.dashboardContainerView.alpha = 0; self.messagesContainerView.alpha = 0; self.patientDataContainerView.alpha = 1})
                patientDataButton.isSelected = true
                UIButton.animate(withDuration: 0.3, animations: {self.patientDataButton.backgroundColor = UIColor(red: 0.2588, green: 0.66667, blue: 0.8745, alpha: 1)})
                let curButton = self.view.viewWithTag(currentButton) as! UIButton
                UIButton.animate(withDuration: 0.3, animations:{ curButton.backgroundColor = UIColor(red: 0.433, green: 0.7843, blue: 0.8941, alpha: 1)})
                currentButton = 3
            }
        } else {
            print("error on button press")
            return
        }
    }
    
    @objc func dismissKeyboard (){
        view.endEditing(true)
    }
    
    func setButton(button: UIButton){
        let imgsize = button.imageView!.frame.size
        let titlesize = button.titleLabel!.frame.size
        let totalHeight = imgsize.height + titlesize.height

        button.imageEdgeInsets = UIEdgeInsets(top: -(totalHeight - imgsize.height), left: 42.5 - (imgsize.width/2), bottom: 0, right: 0)
        button.titleEdgeInsets = UIEdgeInsets(top: 0, left: -imgsize.width, bottom: -(totalHeight - titlesize.height), right: 0)
    }
}

