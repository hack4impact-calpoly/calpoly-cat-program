//
//  dashboardViewController.swift
//  transitions mental health assoc
//
//  Created by Finlay Piroth on 4/7/20.
//  Copyright © 2020 Hack4Impact. All rights reserved.
//

import UIKit

class dashboardViewController: UIViewController {
    
    //MARK: properties
    
    @IBOutlet weak var eventComments: UITextView!
    @IBOutlet weak var eventTime: UITextField!
    @IBOutlet weak var eventDate: UITextField!
    @IBOutlet weak var eventType: UISegmentedControl!
    @IBOutlet weak var submitButton: UIButton!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        NotificationCenter.default.addObserver(self, selector: #selector(keyboardWillShow), name: UIResponder.keyboardWillShowNotification, object: nil)
        NotificationCenter.default.addObserver(self, selector: #selector(keyboardWillHide), name: UIResponder.keyboardWillHideNotification, object: nil)
        
        let tap: UITapGestureRecognizer = UITapGestureRecognizer(target: self, action: #selector(UIInputViewController.dismissKeyboard))
        
        view.addGestureRecognizer(tap)
        // Do any additional setup after loading the view.
    }
    //MARK: functions
    
    @IBAction func submitPressed(_ sender: UIButton) {
        /*let curEvent = Event.init(type: eventType.titleForSegment(at: eventType.selectedSegmentIndex), date: eventDate.text, time: eventTime.text, comments: eventComments.text)*/
    }
    
    @objc func dismissKeyboard (){
        view.endEditing(true)
    }
    
    @objc func keyboardWillShow(notification: NSNotification) {
        if let keyboardSize = (notification.userInfo?[UIResponder.keyboardFrameBeginUserInfoKey] as? NSValue)?.cgRectValue {
            if self.view.frame.origin.y == 0 {
                self.view.frame.origin.y -= keyboardSize.height
            }
        }
    }

    @objc func keyboardWillHide(notification: NSNotification) {
        if self.view.frame.origin.y != 0 {
            self.view.frame.origin.y = 0
        }
    }
    
    struct Event {
        var type: String?
        var date: String?
        var time: String?
        var comments: String?
    }
}
