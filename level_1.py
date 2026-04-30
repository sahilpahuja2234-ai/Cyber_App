import pygame as pg

from menu import NEON_CYAN, PURE_WHITE, draw_box


class LevelOne:
    def __init__(self,score):
        self.score = score
        self.frames = [
            pg.image.load('Graphic/Level_1_graphics/level_1_base_frame.png').convert_alpha(),
            pg.image.load('Graphic/Level_1_graphics/level_1_transition_frame.png').convert_alpha(),
            pg.image.load('Graphic/Level_1_graphics/level_1_final_frame.png').convert_alpha(),
            pg.image.load('Graphic/Level_1_graphics/level_1_final_final_frame.png').convert_alpha(),
        ]
        self.email_view = pg.image.load('Graphic/Level_1_graphics/Email_Opened_view_0 .png').convert_alpha()
        self.back_button = pg.image.load('Graphic/Level_1_graphics/back_button.png').convert_alpha()
        self.report_button = pg.image.load('Graphic/Level_1_graphics/Report_button.png').convert_alpha()

        # Load fonts ONCE in __init__ to save performance
        self.level_1_font = pg.font.Font('Font/Level_1_font/OpenSans-Bold.ttf', 15)
        self.instruction_font = pg.font.Font('Font/Level_1_font/OpenSans_Condensed-Regular.ttf', 70)
        self.open_sender_font = pg.font.Font('Font/Level_1_font/OpenSans_Condensed-Regular.ttf', 20)
        self.open_subject_font = pg.font.Font('Font/Level_1_font/OpenSans_Condensed-Regular.ttf', 28)
        self.open_meta_font = pg.font.Font('Font/Level_1_font/OpenSans_Condensed-Regular.ttf', 16)
        self.open_body_font = pg.font.Font('Font/Level_1_font/OpenSans_Condensed-Regular.ttf', 17)
        self.open_attach_font = pg.font.Font('Font/Level_1_font/OpenSans_Condensed-Regular.ttf', 15)

        self.frame_index = 0
        self.timer = 0

        self.rows_rect = [
            pg.Rect(220, 220, 950, 55),
            pg.Rect(220, 265, 950, 55),
            pg.Rect(220, 317.5, 950, 55),
            pg.Rect(220, 370, 950, 55),
            pg.Rect(220, 428, 950, 55),
            pg.Rect(220, 480, 950, 55),
            pg.Rect(220, 535, 950, 55),
            pg.Rect(220, 590, 950, 55),
            pg.Rect(220, 660, 950, 55)
        ]
        self.check_email_for_score = []
        self.check_back_for_score = []
        self.emails = [
            (
                "HR Dept",
                "Meeting Rescheduled",
                "Shifted to 6:30 PM. Be prepared.",
                "5:12 PM",
                "hr.dept@yourcompany.internal",
                "you@yourcompany.internal",
                [
                    "Hi,",
                    "The team sync originally scheduled for 5:00 PM has been",
                    "moved to 6:30 PM due to a last-minute conference room conflict.",
                    "",
                    "Please update your calendar and come prepared",
                    "with your weekly progress summary.",
                    "",
                    "— HR Department"
                ],
                None,  # no attachment
                False,  # not suspicious
                "keep"  # correct action
            ),
            (
                "IT Support",
                "Password Expiring Soon",
                "Reset within 24 hours.",
                "4:48 PM",
                "it.support@yourcompany.internal",
                "you@yourcompany.internal",
                [
                    "Dear User,",
                    "Your account password will expire in 24 hours.",
                    "",
                    "To reset it, please visit the official IT portal at:",
                    "portal.your_company.internal/reset",
                    "",
                    "Do NOT share your credentials with anyone,",
                    "including IT staff.",
                    "",
                    "— IT Support Team"
                ],
                None,
                False,
                "keep"
            ),
            (
                "Unknown Sender",
                "You missed something...",
                "Check the last attachment again.",
                "4:21 PM",
                "noreply.alert994@gmail.com",
                "you@yourcompany.internal",
                [
                    "Hey,",
                    "I think you left something behind in the last meeting.",
                    "I've attached the file you were looking at.",
                    "",
                    "Just open the attachment — it's safe, trust me.",
                ],
                "notes_final_REAL.exe",  # suspicious attachment
                True,
                "report"
            ),
            (
                "Security Team",
                "Unauthorized Login Attempt",
                "Location mismatch detected.",
                "3:55 PM",
                "security@yourcompany.internal",
                "you@yourcompany.internal",
                [
                    "ALERT: An unauthorized login attempt was detected.",
                    "",
                    "Location : Eastern Europe",
                    "Device   : Unknown — Windows 11",
                    "Time     : 3:47 PM today",
                    "",
                    "If this was NOT you, change your password immediately",
                    "via the IT portal.",
                    "",
                    "Do NOT click any external links regarding this alert."
                ],
                None,
                False,
                "keep"
            ),
            (
                "Project Lead",
                "Final Build Status?",
                "Need update before tonight.",
                "3:10 PM",
                "p.lead@yourcompany.internal",
                "you@yourcompany.internal",
                [
                    "Hey,",
                    "Haven't heard back from the dev team yet.",
                    "We need the final build status confirmed before",
                    "end of day — client is waiting.",
                    "",
                    "Reply directly or update the tracker",
                    "on the internal dashboard.",
                    "",
                    "— Project Lead"
                ],
                None,
                False,
                "keep"
            ),
            (
                "No Reply",
                "System Alert #4421",
                "Background process interrupted.",
                "2:46 PM",
                "no-reply@sys-monitor.net",
                "you@yourcompany.internal",
                [
                    "SYSTEM MONITOR — ALERT #4421",
                    "A background process on your machine was interrupted.",
                    "",
                    "This may affect your work performance.",
                    "To restore full functionality, download the patch:",
                    "",
                    ">>> sys_patch_4421.exe — external link <<<",
                    "",
                    "Failure to act within 1 hour may result in data loss."
                ],
                "sys_patch_4421.exe",
                True,
                "report"
            ),
            (
                "Friend",
                "Game tonight?",
                "Don't ditch again 😑",
                "2:15 PM",
                "alex.r.personal@gmail.com",
                "your.personal@gmail.com",
                [
                    "Bro seriously don't ditch again 😑",
                    "We're starting at 9. Same server as last time.",
                    "",
                    "Just reply yes or no, it's not that deep.",
                    "",
                    "— Alex"
                ],
                None,
                False,
                "keep"
            ),
            (
                "Unknown",
                "OPEN THIS",
                "...you'll understand.",
                "1:22 PM",
                "d4t4_bre4ch@protonmail.com",
                "you@yourcompany.internal",
                [
                    "You need to see this.",
                    "Someone inside your company has been leaking data.",
                    "I have proof.",
                    "",
                    ">>> Click here to view the evidence <<<",
                    "http://dataexpose-secure.ru/view?id=YOU",
                    "",
                    "Don't tell anyone. Act fast."
                ],
                None,
                True,
                "report"
            ),
            (
                "???",
                "You are being watched",
                "Don't trust the system.",
                "11:11 AM",
                "[ENCRYPTED — SENDER UNKNOWN]",
                "[UNDISCLOSED RECIPIENTS]",
                [
                    "We see everything you do.",
                    "Every file. Every login. Every mistake.",
                    "",
                    "The system you trust has already been compromised.",
                    "Your credentials were sold 3 days ago.",
                    "",
                    "This is your only warning.",
                    "Do not reply. Do not report this.",
                    "It won't help."
                ],
                None,
                True,
                "report"
            ),
        ]
        self.instructions = [
            "LEVEL 1: EMAIL INSPECTION",
            "",
            "Open each email and analyze carefully.",
            "Report or delete suspicious emails.",
            "",
            "Correct action = +Points",
            "Wrong report = -10 Points",
            "",
            "At least ONE correct action per email",
            "",
            "Click anywhere or press SPACE to start"
        ]
        # Define the instruction box Rect here so all methods can access it
        self.instruction_rect = pg.Rect(500, 500, 300, 100)
        self.Instruction_read = False
        self.selected_email = None

        self.feedback_timer = 0
        self.feedback_text = ""
        self.feedback_color = (0, 0, 0)

    def opened_email_view(self, i, surface):
        surface.fill((10, 10, 20))
        surface.blit(self.email_view, (0, 0))
        surface.blit(self.back_button, (245, 185))
        surface.blit(self.report_button, (1185, 180))

        email = self.emails[i]

        # Blit all surfaces — THIS was missing
        surface.blit(self.open_subject_font.render(email[1], True, NEON_CYAN), (260, 220))
        surface.blit(self.open_sender_font.render(email[0], True, PURE_WHITE), (260, 260))
        surface.blit(self.open_meta_font.render(f"From: {email[4]}", True, (150, 210, 220)), (260, 290))
        surface.blit(self.open_meta_font.render(f"To:   {email[5]}", True, (150, 210, 220)),(260, 320))  # email[5] not [4]
        surface.blit(self.open_attach_font.render(email[3], True, (140, 140, 140)), (1190, 230))

        # Divider line
        pg.draw.line(surface, (50, 80, 100), (240, 355), (1260, 355), 1)

        # Body loop — email[6] is the list
        for j, line in enumerate(email[6]):
            body_surface = self.open_body_font.render(line, True, (200, 200, 200))
            surface.blit(body_surface, (260, 375 + j * 25))

        # Attachment — email[7]
        if email[7] is not None:
            surface.blit(self.open_attach_font.render(f"📎  {email[7]}", True, (220, 80, 80)), (260, 620))

    def report_scoring_level1(self,i, s):
        if i in s:
            return
        viewed_email = self.emails[i]
        s.append(i)
        if viewed_email[9] == "report":
            self.score.add(20)
            self.feedback_text = "+20  Correct Report!"
            self.feedback_color = (0, 180, 120)
        else:
            self.score.deduct(10)
            self.feedback_text = "-10  Wrong Report!"
            self.feedback_color = (180, 40, 40)
        self.feedback_timer = 120  # show for 120 frames (~2 seconds at 60fps)

    def back_scoring_level1(self, i, s):
        if i in s:
            return
        viewed_email = self.emails[i]
        s.append(i)
        if viewed_email[8] == False:  # safe email, back = correct
            self.score.add(20)
            self.feedback_text = "+20  Safe Email!"
            self.feedback_color = (0, 180, 120)
        else:  # suspicious email, back = wrong
            self.score.deduct(10)
            self.feedback_text = "-10  Should've Reported!"
            self.feedback_color = (180, 40, 40)
        self.feedback_timer = 120

    def handle_event(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                if not self.Instruction_read:
                    self.Instruction_read = True

        if event.type == pg.MOUSEBUTTONDOWN:
            if not self.Instruction_read:
                self.Instruction_read = True
                return

            if self.selected_email is not None:
                back_rect = pg.Rect(245, 185, 120, 50)
                report_rect = pg.Rect(1185, 180, 120, 50)

                if back_rect.collidepoint(event.pos):
                    self.back_scoring_level1(self.selected_email, self.check_back_for_score)
                    self.selected_email = None

                elif report_rect.collidepoint(event.pos):
                    self.report_scoring_level1( self.selected_email, self.check_email_for_score)
                    self.selected_email = None
                return

            for i, rect in enumerate(self.rows_rect):
                if rect.collidepoint(event.pos):
                    self.selected_email = i

    def update(self):
        self.timer += 1
        if self.timer > 15:
            self.timer = 0
            if self.frame_index < len(self.frames) - 1:
                self.frame_index += 1

        if self.feedback_timer > 0:
            self.feedback_timer -= 1  # ← add this

    def draw(self, surface):
        surface.fill((0, 0, 0))

        if not self.Instruction_read:
            surface.fill((10, 10, 20))
            for i, line in enumerate(self.instructions):
                if i == 0:
                    text_surface = self.instruction_font.render(line, True, (0, 255, 180))
                else:
                    text_surface = self.level_1_font.render(line, True, (200, 200, 200))
                surface.blit(text_surface, (200, 150 + i * 40))
            return

        if self.selected_email is not None:
            self.opened_email_view(self.selected_email, surface)
            return

        # Inbox view
        surface.blit(self.frames[self.frame_index], (0, 0))
        mouse_pos = pg.mouse.get_pos()

        for i, rect in enumerate(self.rows_rect):
            if rect.collidepoint(mouse_pos):
                pg.draw.rect(surface, (0, 120, 140), rect)
            email = self.emails[i]
            surface.blit(self.level_1_font.render(email[0], True, (200, 230, 245)), (rect.x + 60, rect.y + 10))
            surface.blit(self.level_1_font.render(email[1], True, (200, 230, 245)), (rect.x + 240, rect.y + 10))
            surface.blit(self.level_1_font.render(email[2], True, (140, 180, 200)), (rect.x + 240, rect.y + 30))
            surface.blit(self.level_1_font.render(email[3], True, (110, 150, 170)), (rect.x + 880, rect.y + 15))

        # ← feedback box shown on inbox, visible after email closes
        if self.feedback_timer > 0:
            draw_box(
                surface,
                color=self.feedback_color,
                rect=pg.Rect(480, 300, 320, 90),
                text=self.feedback_text,
                text_color=PURE_WHITE,
                font=self.open_sender_font
            )