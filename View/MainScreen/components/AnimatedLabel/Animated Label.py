from kivymd.uix.label import MDLabel


class AnimatedLabel(MDLabel):
    LETTER_DELAY = 0.03
    FADE_DURATION = 0.08

    def __init__(self,*args, **kwargs):
        self._clock_events = []
        self._alphas = []
        self._target_text = ""
        self._rgb_hex = []
        super().__init__(**kwargs)

    def set_text(self, full_text):
        for ev in self._clock_events:
            ev.cancel()
        self._clock_events.clear()
        c = self.parent.parent.ids.top_title.color
        self._rgb_hex = "#{:02x}{:02x}{:02x}".format(
            int(c[0] * 255),
            int(c[1] * 255),
            int(c[2] * 255),
        )
        self._target_text = full_text
        self._alphas = [0.0] * len(full_text)
        self._rebuild_markup()
        for i in range(len(full_text)):
            ev = Clock.schedule_once(
                lambda dt, idx=i: self._fade_letter(idx),
                i * self.LETTER_DELAY,
            )
            self._clock_events.append(ev)

    def _rebuild_markup(self):
        result = []
        for i, ch in enumerate(self._target_text):
            alpha = int(self._alphas[i] * 255)
            hex_a = format(alpha, '02x')
            result.append("[color={}{}]{}[/color]".format(self._rgb_hex, hex_a, ch))
        self.parent.parent.ids.top_title.text = "".join(result)

    def _fade_letter(self, idx):
        steps = 10
        step_dur = self.FADE_DURATION / steps
        counter = [0]

        def tick(dt):
            counter[0] += 1
            self._alphas[idx] = min(1.0, counter[0] / steps)
            self._rebuild_markup()
            if counter[0] >= steps:
                return False

        ev = Clock.schedule_interval(tick, step_dur)
        self._clock_events.append(ev)
