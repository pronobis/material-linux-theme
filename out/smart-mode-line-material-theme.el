;;; smart-mode-line-material-theme.el --- Material theme for smart-mode-line
;;; Commentary:
;;; Code:

(deftheme smart-mode-line-material
  "Material theme for smart-mode-line.
   Mimics the appearance of powerline.")

(require 'powerline)

(let ((separator-left
       '(intern (format "powerline-%s-%s"
                        powerline-default-separator
                        (car powerline-default-separator-dir))))
      (separator-right
       '(intern (format "powerline-%s-%s"
                        powerline-default-separator
                        (cdr powerline-default-separator-dir)))))

  (custom-theme-set-faces
   'smart-mode-line-material
   `(sml/global            ((t :background "#1f1f1f")))

   ;; 1) - Positions etc.
   ;; Use fringe/like sml/global as default face
   `(sml/line-number       ((t :inherit sml/global                                                          :weight bold)))
   `(sml/col-number        ((t :inherit sml/global                                                                      )))
   `(sml/remote            ((t :inherit sml/global                                                                      )))
   `(sml/numbers-separator ((t :inherit sml/global                                                                      )))
   `(sml/client            ((t :inherit sml/global                                                                      )))
   `(sml/mule-info         ((t :inherit sml/global                                                                      )))
   `(sml/not-modified      ((t :inherit sml/global                                                                      )))
   `(sml/modified          ((t :background "#ff2d6f" :foreground "#1f1f1f" :weight bold)))
   `(sml/outside-modified  ((t :background "#e84e40"         :foreground "#1f1f1f" :weight bold)))
   '(sml/read-only         ((t :background "#2baf2b" :foreground "#1f1f1f" :weight bold)))

   ;; 2) - ID
   ;; Don't specify default face, use natural modeline background instead
   `(sml/prefix     ((t :foreground "#9ccc65"        )))
   `(sml/projectile ((t :foreground "#9ccc65"        )))
   `(sml/filename   ((t :foreground "#ffc400"   )))
   `(sml/sudo       ((t :foreground "#ff2d6f"    )))
   `(sml/folder     ((t :foreground "#ffffff")))

   ;; 3) - Empty filling combined with some info.
   ;; Use fringe/like sml/global as default face
   `(sml/name-filling        ((t :inherit sml/global                                        )))
   `(sml/position-percentage ((t :inherit sml/global                                        )))
   `(sml/vc                  ((t :inherit sml/global :foreground "#ffc400")))
   `(sml/vc-edited           ((t :inherit sml/global :foreground "#ff2d6f" )))

   ;; 4) - Major Mode
   ;; Don't specify default face, use natural modeline background instead
   `(sml/modes               ((t :weight bold                                                  )))
   `(sml/process             ((t :inherit sml/modes :foreground "#d4e157")))

   ;; 5) Minor Modes.
   ;; Use fringe/like sml/global as default face
   ;; minor modes
   `(sml/minor-modes         ((t :inherit sml/global)))


   ;; 6) Additional info
   ;; Use fringe/like sml/global as default face
   `(sml/discharging         ((t :inherit sml/global :foreground "#ff2d6f")))
   `(sml/time                ((t :inherit sml/global)))

   )

  (custom-theme-set-variables
   'smart-mode-line-material
   '(sml/mode-width (if (eq powerline-default-separator 'arrow) 'right 'full))
   `(sml/pre-id-separator
     '(""
       (:propertize " " face fringe)
       (:eval (propertize " " 'display (funcall ,separator-left 'fringe 'nil)))
       (:propertize " " )))
   `(sml/pos-id-separator
     '(""
       (:propertize " " )
       (:eval (propertize " " 'display (funcall ,separator-left 'nil 'fringe)))
       (:propertize " " face fringe)))
   `(sml/pre-modes-separator
     '(""
       (:propertize " " face fringe)
       (:eval (propertize " " 'display (funcall ,separator-left 'fringe 'nil)))
       (:propertize " " )))
   `(sml/pre-minor-modes-separator
     '(""
       (:propertize " " )
       (:eval (propertize " " 'display (funcall ,separator-right 'nil 'fringe)))
       (:propertize " " face fringe)))
   `(sml/pos-minor-modes-separator
     '("" (:propertize " " face fringe)
       (:eval (propertize " " 'display (funcall ,separator-right 'fringe 'fringe)))
       (:propertize " " face fringe))) ))

;;;###autoload
(when load-file-name
  (add-to-list 'custom-theme-load-path
               (file-name-as-directory (file-name-directory load-file-name))))

(provide-theme 'smart-mode-line-material)
;;; smart-mode-line-material-theme.el ends here.
