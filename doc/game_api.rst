========
Game API
========

Arcade currently has two modes of development:

- *Function-oriented*. You draw on the screen by calling arcade functions
  and writing your own functions. Useful for people that don't know much
  Python, or if you're dabbling interactively.

- *Class-oriented*. You subclass from ``arcade.Window`` and follow a
  ``pyglet`` style of development by filling in magic method for pyglet
  and reading the pyglet API. Pyglet then directly calls your methods.
  If you plan to write an actual game, this is the route you'll go.

The ``arcade.Game`` API replaces the second of these with two changes:

- *Arcade is in charge*. Instead of following the pyglet API, Arcade
  developers follow an Arcade-managed API. Arcade then calls your code,
  acting as a mediator between pyglet and your game. Thus, you think in
  terms of writing a game and not working with a window.

- *Eliminate noise*. Arcade has done a very good job on hiding some of
  the pyglet pain. But parts remain: we have a global window variable,
  users have to call ``start_render``, etc.

As a further goal, we might be able to do things such as greatly improve
performance via OpenGL batching without the user needing to know much about
it (implicit batching.)

How It Works
============

In this proposal, users write a game by subclassing from ``arcade.Game``.
Its constructor, behind the scenes, makes an instance of
``arcade.GameWindow`` (which is a ``pyglet.window.Window``) and stores
it as an attribute on the ``Game`` instance. Ideally, users never need
to touch this pyglet window.

Next is the important part. The ``Game`` constructor passes its instance
into the ``GameWindow`` constructor. This allows the ``GameWindow``
event handlers -- pyglet mouse and key events, for example -- to call
the methods in the arcade Game API.

Notes
=====

- There are several games in ``arcade.examples`` prefaced with ``game_``
  that show the simplest hello world, event handling, etc.

To Do
=====

- Investigate making ``arcade.Game`` into an abstract base class

- Use inspection to see if you should pass in key_modifiers
