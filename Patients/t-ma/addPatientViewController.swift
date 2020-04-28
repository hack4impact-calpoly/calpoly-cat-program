//
//  addPatientViewController.swift
//  transitions mental health assoc
//
//  Created by Finlay Piroth on 4/14/20.
//  Copyright © 2020 Hack4Impact. All rights reserved.
//

import UIKit

class addPatientViewController: UIViewController {
    
    //MARK: properties
    
    @IBOutlet weak var lnameTextField: UITextField!
    @IBOutlet weak var fnameTextField: UITextField!
    
    @IBOutlet weak var birthdayTextField: UITextField!
    @IBOutlet weak var locationTextField: UITextField!
    @IBOutlet weak var phoneTextField: UITextField!
    @IBOutlet weak var emailTextField: UITextField!
    @IBOutlet weak var notesTextView: UITextView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
               
        NotificationCenter.default.addObserver(self, selector: #selector(keyboardWillShow), name: UIResponder.keyboardWillShowNotification, object: nil)
        NotificationCenter.default.addObserver(self, selector: #selector(keyboardWillHide), name: UIResponder.keyboardWillHideNotification, object: nil)
    }
    
    @objc func keyboardWillShow(notification: NSNotification) {
        if let keyboardSize = (notification.userInfo?[UIResponder.keyboardFrameBeginUserInfoKey] as? NSValue)?.cgRectValue {
            if self.view.frame.origin.y == 0 {
                self.view.frame.origin.y -= (keyboardSize.height - 150)
            }
            
        }
    }

    @objc func keyboardWillHide(notification: NSNotification) {
        if self.view.frame.origin.y != 0 {
            self.view.frame.origin.y = 0
        }
    }
    
    @IBAction func submitClick(_ sender: Any) {
        if(fnameTextField.hasText && lnameTextField.hasText && birthdayTextField.hasText && locationTextField.hasText && phoneTextField.hasText && emailTextField.hasText){
            let fname = fnameTextField.text ?? "not provided"
            let lname = lnameTextField.text ?? "not provided"
            let bday = birthdayTextField.text ?? "not provided"
            let loc = locationTextField.text ?? "not provided"
            let phone = phoneTextField.text ?? "not provided"
            let email = emailTextField.text ?? "not provided"
            let notes = notesTextView.text ?? "not provided"
            let url = URL(string: "https://tmha-backend.herokuapp.com/api/clients/")
            guard let requestURL = url else {
                fatalError()
            }
            var request = URLRequest(url: requestURL)
            request.httpMethod = "POST"
            
            let postString = "first_name=\(fname)&last_name=\(lname)&birthday=\(bday)&location=\(loc)&phone=\(phone)&email=\(email)&notes=\(notes)"
            request.httpBody = postString.data(using: String.Encoding.utf8)
            let task = URLSession(configuration: URLSessionConfiguration.default).dataTask(with: request) {(data, response, error) in
                if let error = error {
                    print("Error occured \(error)")
                    return
                }
                
                if let data = data, let dataString = String(data: data, encoding: .utf8) {
                    print("Response data string:\n \(dataString)")
                }
            }
            task.resume()
            fnameTextField.text = ""
            lnameTextField.text = ""
            birthdayTextField.text = ""
            locationTextField.text = ""
            phoneTextField.text = ""
            emailTextField.text = ""
            notesTextView.text = ""
            let alert = UIAlertController(title: "Form Submitted!", message: "form has been submitted successfully", preferredStyle: .alert)
            alert.addAction(UIAlertAction(title: "Done", style: .default, handler: nil))
            self.present(alert, animated: true)
            
        } else {
            let alert = UIAlertController(title: "Unfinished form", message: "Please make sure all fields are filled out", preferredStyle: .alert)
            alert.addAction(UIAlertAction(title: "OK", style: .default, handler: nil))
            self.present(alert, animated: true)
        }
        
        
    }
    
}
