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
   `(sml/global            ((t :background "[material:window-bg]")))

   ;; 1) - Positions etc.
   ;; Use fringe/like sml/global as default face
   `(sml/line-number       ((t :inherit sml/global                                                          :weight bold)))
   `(sml/col-number        ((t :inherit sml/global                                                                      )))
   `(sml/remote            ((t :inherit sml/global                                                                      )))
   `(sml/numbers-separator ((t :inherit sml/global                                                                      )))
   `(sml/client            ((t :inherit sml/global                                                                      )))
   `(sml/mule-info         ((t :inherit sml/global                                                                      )))
   `(sml/not-modified      ((t :inherit sml/global                                                                      )))
   `(sml/modified          ((t :background "[material:file-modified-tx]" :foreground "[material:window-bg]" :weight bold)))
   `(sml/outside-modified  ((t :background "[material:error-tx]"         :foreground "[material:window-bg]" :weight bold)))
   '(sml/read-only         ((t :background "[material:file-readonly-tx]" :foreground "[material:window-bg]" :weight bold)))

   ;; 2) - ID
   ;; Don't specify default face, use natural modeline background instead
   `(sml/prefix     ((t :foreground "[material:semantic4]"        )))
   `(sml/projectile ((t :foreground "[material:semantic4]"        )))
   `(sml/filename   ((t :foreground "[material:accent2-normal]"   )))
   `(sml/sudo       ((t :foreground "[material:accent-normal]"    )))
   `(sml/folder     ((t :foreground "[material:file-directory-tx]")))

   ;; 3) - Empty filling combined with some info.
   ;; Use fringe/like sml/global as default face
   `(sml/name-filling        ((t :inherit sml/global                                        )))
   `(sml/position-percentage ((t :inherit sml/global                                        )))
   `(sml/vc                  ((t :inherit sml/global :foreground "[material:accent2-normal]")))
   `(sml/vc-edited           ((t :inherit sml/global :foreground "[material:file-modified-tx]" )))

   ;; 4) - Major Mode
   ;; Don't specify default face, use natural modeline background instead
   `(sml/modes               ((t :weight bold                                                  )))
   `(sml/process             ((t :inherit sml/modes :foreground "[material:file-executable-tx]")))

   ;; 5) Minor Modes.
   ;; Use fringe/like sml/global as default face
   ;; minor modes
   `(sml/minor-modes         ((t :inherit sml/global)))


   ;; 6) Additional info
   ;; Use fringe/like sml/global as default face
   `(sml/discharging         ((t :inherit sml/global :foreground "[material:accent-normal]")))
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
