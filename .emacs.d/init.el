(setq inhibit-startup-message t)

(setq c-default-style "bsd"
      c-basic-offset 8
      tab-width 8
      indent-tabs-mode t)

(require 'whitespace)
(setq whitespace-style '(face empty lines-tail trailing))
(global-whitespace-mode t)

(setq column-number-mode t)

(menu-bar-mode -1)
(scroll-bar-mode -1)
(tool-bar-mode -1)
(blink-cursor-mode -1)

(if window-system
    (load-theme 'solarized-light t)
  (load-theme 'wombat t))

(delete-selection-mode t)
(transient-mark-mode t)
(setq x-select-enable-clipboard t)

(setq-default indicate-empty-lines t)
(when (not indicate-empty-lines)
  (toggle-indicate-empty-lines))

(global-hl-line-mode +1)
(line-number-mode +1)
(column-number-mode t)
(size-indication-mode t)

(setq-default show-trailing-whitespace t)
