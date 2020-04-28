//
//  test2.swift
//  transitions mental health assoc
//
//  Created by Finlay Piroth on 3/28/20.
//  Copyright © 2020 Hack4Impact. All rights reserved.
//

import UIKit

class test2: UIViewController {

    @IBOutlet weak var patientdataButton: UIButton!
    @IBOutlet weak var messagesButton: UIButton!
    @IBOutlet weak var dashboardButton: UIButton!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setButton(button: patientdataButton)
        setButton(button: messagesButton)
        setButton(button: dashboardButton)

        // Do any additional setup after loading the view.
    }

    func setButton(button: UIButton){
        let imgsize = button.imageView!.frame.size
        let titlesize = button.titleLabel!.frame.size
        let totalHeight = imgsize.height + titlesize.height

        button.imageEdgeInsets = UIEdgeInsets(top: -(totalHeight - imgsize.height), left: 0, bottom: 0, right: -titlesize.width)
        button.titleEdgeInsets = UIEdgeInsets(top: 0, left: -imgsize.width, bottom: -(totalHeight - titlesize.height), right: 0)
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
