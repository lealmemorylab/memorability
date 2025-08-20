#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Mon Jun  6 11:10:17 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'Mem_Test2'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data_test2/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/fernanda/Library/CloudStorage/Box-Box/Leal Lab/Behavioral Tasks/In-Person Tasks/Memorability/memorability/test2.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
Instructions = visual.TextStim(win=win, name='Instructions',
    text='Now we’ll be testing your memory for the images you saw earlier\n\n\nV = Exact same \nN = New / Different \n\n\nThe image will be on the screen for 3 seconds. Be sure to respond while the image is on the screen.\n\nPress the space bar for examples',
    font='Arial',
    pos=[0, 0], height=0.09, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instruction_key = keyboard.Keyboard()

# Initialize components for Routine "pic"
picClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='example1.jpg', mask=None,
    ori=0.0, pos=(0, 0), size=[1,1],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
text_2 = visual.TextStim(win=win, name='text_2',
    text='Imagine this is an image you saw earlier\n',
    font='Open Sans',
    pos=(0, -.7), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "Examples"
ExamplesClock = core.Clock()
example_image = visual.ImageStim(
    win=win,
    name='example_image', 
    image='sin', mask=None,
    ori=0.0, pos=(0,0), size=[1,1],
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=512.0, interpolate=True, depth=0.0)
example_key = keyboard.Keyboard()
text = visual.TextStim(win=win, name='text',
    text='V = EXACT SAME    N = NEW / DIFFERENT',
    font='Arial',
    pos=(0, -.7), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "StartScreen"
StartScreenClock = core.Clock()
start_text = visual.TextStim(win=win, name='start_text',
    text='The test will now start\n\nThis will take about 15 minutes\n\nThere will be a break halfway through\n\nAny questions?\n\nPress the space bar to begin',
    font='Open Sans',
    pos=(0, 0), height=0.12, wrapWidth=1.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
start_key = keyboard.Keyboard()

# Initialize components for Routine "test"
testClock = core.Clock()
ISI = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
Stimuli = visual.ImageStim(
    win=win,
    name='Stimuli', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
Key_Response = keyboard.Keyboard()
text_4 = visual.TextStim(win=win, name='text_4',
    text='V = EXACT SAME    N = NEW / DIFFERENT',
    font='Arial',
    pos=(0, -.8), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "pause"
pauseClock = core.Clock()
Pause_text = visual.TextStim(win=win, name='Pause_text',
    text='You can take a quick break\n\nInstructions are the same \n\nV = Exact same\nN = New/Different\n\nPress the space bar to continue\n',
    font='Arial',
    pos=[0, 0], height=0.08, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Space = keyboard.Keyboard()

# Initialize components for Routine "test"
testClock = core.Clock()
ISI = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
Stimuli = visual.ImageStim(
    win=win,
    name='Stimuli', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
Key_Response = keyboard.Keyboard()
text_4 = visual.TextStim(win=win, name='text_4',
    text='V = EXACT SAME    N = NEW / DIFFERENT',
    font='Arial',
    pos=(0, -.8), height=0.07, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "END"
ENDClock = core.Clock()
End_text = visual.TextStim(win=win, name='End_text',
    text='END OF THE TEST \n\nPlease go get your experimenter\n\nTHANK YOU',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=1.5, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructions"-------
continueRoutine = True
# update component parameters for each repeat
instruction_key.keys = []
instruction_key.rt = []
_instruction_key_allKeys = []
# keep track of which components have finished
instructionsComponents = [Instructions, instruction_key]
for thisComponent in instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instructions* updates
    if Instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instructions.frameNStart = frameN  # exact frame index
        Instructions.tStart = t  # local t and not account for scr refresh
        Instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instructions, 'tStartRefresh')  # time at next scr refresh
        Instructions.setAutoDraw(True)
    
    # *instruction_key* updates
    if instruction_key.status == NOT_STARTED and t >= 3-frameTolerance:
        # keep track of start time/frame for later
        instruction_key.frameNStart = frameN  # exact frame index
        instruction_key.tStart = t  # local t and not account for scr refresh
        instruction_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instruction_key, 'tStartRefresh')  # time at next scr refresh
        instruction_key.status = STARTED
        # keyboard checking is just starting
        instruction_key.clock.reset()  # now t=0
    if instruction_key.status == STARTED:
        theseKeys = instruction_key.getKeys(keyList=['space'], waitRelease=False)
        _instruction_key_allKeys.extend(theseKeys)
        if len(_instruction_key_allKeys):
            instruction_key.keys = _instruction_key_allKeys[-1].name  # just the last key pressed
            instruction_key.rt = _instruction_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "pic"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
picComponents = [image, text_2, key_resp]
for thisComponent in picComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
picClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "pic"-------
while continueRoutine:
    # get current time
    t = picClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=picClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in picComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "pic"-------
for thisComponent in picComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "pic" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('example_test2.xlsx', selection='0:5'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Examples"-------
    continueRoutine = True
    # update component parameters for each repeat
    example_key.keys = []
    example_key.rt = []
    _example_key_allKeys = []
    # keep track of which components have finished
    ExamplesComponents = [example_image, example_key, text]
    for thisComponent in ExamplesComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ExamplesClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Examples"-------
    while continueRoutine:
        # get current time
        t = ExamplesClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ExamplesClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *example_image* updates
        if example_image.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
            # keep track of start time/frame for later
            example_image.frameNStart = frameN  # exact frame index
            example_image.tStart = t  # local t and not account for scr refresh
            example_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(example_image, 'tStartRefresh')  # time at next scr refresh
            example_image.setAutoDraw(True)
        if example_image.status == STARTED:  # only update if drawing
            example_image.setImage(stim1, log=False)
        
        # *example_key* updates
        if example_key.status == NOT_STARTED and t >= 1-frameTolerance:
            # keep track of start time/frame for later
            example_key.frameNStart = frameN  # exact frame index
            example_key.tStart = t  # local t and not account for scr refresh
            example_key.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(example_key, 'tStartRefresh')  # time at next scr refresh
            example_key.status = STARTED
            # keyboard checking is just starting
            example_key.clock.reset()  # now t=0
        if example_key.status == STARTED:
            theseKeys = example_key.getKeys(keyList=['v', 'n', 'V', 'N'], waitRelease=False)
            _example_key_allKeys.extend(theseKeys)
            if len(_example_key_allKeys):
                example_key.keys = _example_key_allKeys[-1].name  # just the last key pressed
                example_key.rt = _example_key_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ExamplesComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Examples"-------
    for thisComponent in ExamplesComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Examples" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1.0 repeats of 'trials'


# ------Prepare to start Routine "StartScreen"-------
continueRoutine = True
# update component parameters for each repeat
start_key.keys = []
start_key.rt = []
_start_key_allKeys = []
# keep track of which components have finished
StartScreenComponents = [start_text, start_key]
for thisComponent in StartScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
StartScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "StartScreen"-------
while continueRoutine:
    # get current time
    t = StartScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=StartScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *start_text* updates
    if start_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_text.frameNStart = frameN  # exact frame index
        start_text.tStart = t  # local t and not account for scr refresh
        start_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_text, 'tStartRefresh')  # time at next scr refresh
        start_text.setAutoDraw(True)
    
    # *start_key* updates
    if start_key.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start_key.frameNStart = frameN  # exact frame index
        start_key.tStart = t  # local t and not account for scr refresh
        start_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start_key, 'tStartRefresh')  # time at next scr refresh
        start_key.status = STARTED
        # keyboard checking is just starting
        start_key.clock.reset()  # now t=0
    if start_key.status == STARTED:
        theseKeys = start_key.getKeys(keyList=['space'], waitRelease=False)
        _start_key_allKeys.extend(theseKeys)
        if len(_start_key_allKeys):
            start_key.keys = _start_key_allKeys[-1].name  # just the last key pressed
            start_key.rt = _start_key_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in StartScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "StartScreen"-------
for thisComponent in StartScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "StartScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Test = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('StimData_test2.xlsx', selection='0:121'),
    seed=None, name='Test')
thisExp.addLoop(Test)  # add the loop to the experiment
thisTest = Test.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTest.rgb)
if thisTest != None:
    for paramName in thisTest:
        exec('{} = thisTest[paramName]'.format(paramName))

for thisTest in Test:
    currentLoop = Test
    # abbreviate parameter names if possible (e.g. rgb = thisTest.rgb)
    if thisTest != None:
        for paramName in thisTest:
            exec('{} = thisTest[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "test"-------
    continueRoutine = True
    routineTimer.add(3.500000)
    # update component parameters for each repeat
    Key_Response.keys = []
    Key_Response.rt = []
    _Key_Response_allKeys = []
    # keep track of which components have finished
    testComponents = [ISI, Stimuli, Key_Response, text_4]
    for thisComponent in testComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    testClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "test"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = testClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=testClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Stimuli* updates
        if Stimuli.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
            # keep track of start time/frame for later
            Stimuli.frameNStart = frameN  # exact frame index
            Stimuli.tStart = t  # local t and not account for scr refresh
            Stimuli.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Stimuli, 'tStartRefresh')  # time at next scr refresh
            Stimuli.setAutoDraw(True)
        if Stimuli.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Stimuli.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                Stimuli.tStop = t  # not accounting for scr refresh
                Stimuli.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Stimuli, 'tStopRefresh')  # time at next scr refresh
                Stimuli.setAutoDraw(False)
        if Stimuli.status == STARTED:  # only update if drawing
            Stimuli.setImage(Stim, log=False)
        
        # *Key_Response* updates
        waitOnFlip = False
        if Key_Response.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
            # keep track of start time/frame for later
            Key_Response.frameNStart = frameN  # exact frame index
            Key_Response.tStart = t  # local t and not account for scr refresh
            Key_Response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Key_Response, 'tStartRefresh')  # time at next scr refresh
            Key_Response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Key_Response.clock.reset)  # t=0 on next screen flip
        if Key_Response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Key_Response.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                Key_Response.tStop = t  # not accounting for scr refresh
                Key_Response.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Key_Response, 'tStopRefresh')  # time at next scr refresh
                Key_Response.status = FINISHED
        if Key_Response.status == STARTED and not waitOnFlip:
            theseKeys = Key_Response.getKeys(keyList=['n', 'v', 'V', 'N'], waitRelease=False)
            _Key_Response_allKeys.extend(theseKeys)
            if len(_Key_Response_allKeys):
                Key_Response.keys = _Key_Response_allKeys[0].name  # just the first key pressed
                Key_Response.rt = _Key_Response_allKeys[0].rt
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                text_4.setAutoDraw(False)
        # *ISI* period
        if ISI.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            ISI.frameNStart = frameN  # exact frame index
            ISI.tStart = t  # local t and not account for scr refresh
            ISI.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISI, 'tStartRefresh')  # time at next scr refresh
            ISI.start(1)
        elif ISI.status == STARTED:  # one frame should pass before updating params and completing
            ISI.complete()  # finish the static period
            ISI.tStop = ISI.tStart + 1  # record stop time
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "test"-------
    for thisComponent in testComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Test.addData('ISI.started', ISI.tStart)
    Test.addData('ISI.stopped', ISI.tStop)
    Test.addData('Stimuli.started', Stimuli.tStartRefresh)
    Test.addData('Stimuli.stopped', Stimuli.tStopRefresh)
    # check responses
    if Key_Response.keys in ['', [], None]:  # No response was made
        Key_Response.keys = None
    Test.addData('Key_Response.keys',Key_Response.keys)
    if Key_Response.keys != None:  # we had a response
        Test.addData('Key_Response.rt', Key_Response.rt)
    Test.addData('Key_Response.started', Key_Response.tStartRefresh)
    Test.addData('Key_Response.stopped', Key_Response.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'Test'


# ------Prepare to start Routine "pause"-------
continueRoutine = True
# update component parameters for each repeat
Space.keys = []
Space.rt = []
_Space_allKeys = []
# keep track of which components have finished
pauseComponents = [Pause_text, Space]
for thisComponent in pauseComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
pauseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "pause"-------
while continueRoutine:
    # get current time
    t = pauseClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=pauseClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Pause_text* updates
    if Pause_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Pause_text.frameNStart = frameN  # exact frame index
        Pause_text.tStart = t  # local t and not account for scr refresh
        Pause_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Pause_text, 'tStartRefresh')  # time at next scr refresh
        Pause_text.setAutoDraw(True)
    
    # *Space* updates
    if Space.status == NOT_STARTED and t >= 3-frameTolerance:
        # keep track of start time/frame for later
        Space.frameNStart = frameN  # exact frame index
        Space.tStart = t  # local t and not account for scr refresh
        Space.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Space, 'tStartRefresh')  # time at next scr refresh
        Space.status = STARTED
        # keyboard checking is just starting
        Space.clock.reset()  # now t=0
    if Space.status == STARTED:
        theseKeys = Space.getKeys(keyList=['space'], waitRelease=False)
        _Space_allKeys.extend(theseKeys)
        if len(_Space_allKeys):
            Space.keys = _Space_allKeys[-1].name  # just the last key pressed
            Space.rt = _Space_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pauseComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "pause"-------
for thisComponent in pauseComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "pause" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
test2 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('StimData_test2.xlsx', selection='121:242'),
    seed=None, name='test2')
thisExp.addLoop(test2)  # add the loop to the experiment
thisTest2 = test2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTest2.rgb)
if thisTest2 != None:
    for paramName in thisTest2:
        exec('{} = thisTest2[paramName]'.format(paramName))

for thisTest2 in test2:
    currentLoop = test2
    # abbreviate parameter names if possible (e.g. rgb = thisTest2.rgb)
    if thisTest2 != None:
        for paramName in thisTest2:
            exec('{} = thisTest2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "test"-------
    continueRoutine = True
    routineTimer.add(3.500000)
    # update component parameters for each repeat
    Key_Response.keys = []
    Key_Response.rt = []
    _Key_Response_allKeys = []
    # keep track of which components have finished
    testComponents = [ISI, Stimuli, Key_Response, text_4]
    for thisComponent in testComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    testClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "test"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = testClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=testClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Stimuli* updates
        if Stimuli.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
            # keep track of start time/frame for later
            Stimuli.frameNStart = frameN  # exact frame index
            Stimuli.tStart = t  # local t and not account for scr refresh
            Stimuli.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Stimuli, 'tStartRefresh')  # time at next scr refresh
            Stimuli.setAutoDraw(True)
        if Stimuli.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Stimuli.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                Stimuli.tStop = t  # not accounting for scr refresh
                Stimuli.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Stimuli, 'tStopRefresh')  # time at next scr refresh
                Stimuli.setAutoDraw(False)
        if Stimuli.status == STARTED:  # only update if drawing
            Stimuli.setImage(Stim, log=False)
        
        # *Key_Response* updates
        waitOnFlip = False
        if Key_Response.status == NOT_STARTED and tThisFlip >= .5-frameTolerance:
            # keep track of start time/frame for later
            Key_Response.frameNStart = frameN  # exact frame index
            Key_Response.tStart = t  # local t and not account for scr refresh
            Key_Response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Key_Response, 'tStartRefresh')  # time at next scr refresh
            Key_Response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Key_Response.clock.reset)  # t=0 on next screen flip
        if Key_Response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Key_Response.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                Key_Response.tStop = t  # not accounting for scr refresh
                Key_Response.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Key_Response, 'tStopRefresh')  # time at next scr refresh
                Key_Response.status = FINISHED
        if Key_Response.status == STARTED and not waitOnFlip:
            theseKeys = Key_Response.getKeys(keyList=['n', 'v', 'V', 'N'], waitRelease=False)
            _Key_Response_allKeys.extend(theseKeys)
            if len(_Key_Response_allKeys):
                Key_Response.keys = _Key_Response_allKeys[0].name  # just the first key pressed
                Key_Response.rt = _Key_Response_allKeys[0].rt
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + 3.5-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                text_4.setAutoDraw(False)
        # *ISI* period
        if ISI.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            ISI.frameNStart = frameN  # exact frame index
            ISI.tStart = t  # local t and not account for scr refresh
            ISI.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISI, 'tStartRefresh')  # time at next scr refresh
            ISI.start(1)
        elif ISI.status == STARTED:  # one frame should pass before updating params and completing
            ISI.complete()  # finish the static period
            ISI.tStop = ISI.tStart + 1  # record stop time
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "test"-------
    for thisComponent in testComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    test2.addData('ISI.started', ISI.tStart)
    test2.addData('ISI.stopped', ISI.tStop)
    test2.addData('Stimuli.started', Stimuli.tStartRefresh)
    test2.addData('Stimuli.stopped', Stimuli.tStopRefresh)
    # check responses
    if Key_Response.keys in ['', [], None]:  # No response was made
        Key_Response.keys = None
    test2.addData('Key_Response.keys',Key_Response.keys)
    if Key_Response.keys != None:  # we had a response
        test2.addData('Key_Response.rt', Key_Response.rt)
    test2.addData('Key_Response.started', Key_Response.tStartRefresh)
    test2.addData('Key_Response.stopped', Key_Response.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'test2'


# ------Prepare to start Routine "END"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
ENDComponents = [End_text]
for thisComponent in ENDComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ENDClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "END"-------
while continueRoutine:
    # get current time
    t = ENDClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ENDClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *End_text* updates
    if End_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        End_text.frameNStart = frameN  # exact frame index
        End_text.tStart = t  # local t and not account for scr refresh
        End_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(End_text, 'tStartRefresh')  # time at next scr refresh
        End_text.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ENDComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "END"-------
for thisComponent in ENDComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "END" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
