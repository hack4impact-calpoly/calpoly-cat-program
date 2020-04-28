//
//  containertesting.swift
//  transitions mental health assoc
//
//  Created by Finlay Piroth on 4/7/20.
//  Copyright © 2020 Hack4Impact. All rights reserved.
//

import UIKit

class containertesting: UIViewController {
    @IBOutlet weak var containerA: UIView!
    @IBOutlet weak var containerB: UIView!
    var selectedButton = 0
    @IBOutlet weak var buttonA: UIButton!
    @IBOutlet weak var buttonB: UIButton!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        buttonA.tag = 1
        buttonB.tag = 2
        // Do any additional setup after loading the view.
    }
    
    @IBAction func buttonAPress(_ sender: UIButton) {
        if sender.tag == 1 {
            if selectedButton == 1 {
                return
            } else {
                UIView.animate(withDuration: 0.5, animations:{self.containerA.alpha = 1; self.containerB.alpha = 0 })
                selectedButton = 1
            }
        } else {
            if selectedButton == 2 {
                return
            } else {
                UIView.animate(withDuration: 0.5, animations:{self.containerA.alpha = 0; self.containerB.alpha = 1 })
                selectedButton = 2
            }
        }
    }
    
    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */

}
