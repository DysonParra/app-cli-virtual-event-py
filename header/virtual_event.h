#ifndef VIRTUAL_EVENT_H_

#define VIRTUAL_EVENT_H_

/* Includes for the header file */

#ifdef __cplusplus
#define LANGUAGE extern "C"
#elif defined __GNUC__
#define LANGUAGE extern
#endif

#ifdef VIRTUAL_EVENT_STATIC_
#define DLLIMPORT
#elif defined BUILDING
#define DLLIMPORT __declspec(dllexport)
#else
#define DLLIMPORT __declspec(dllimport)
#endif

#define CALLING __cdecl
//#define CALLING __stdcall

/* Macros and definitions for the source file. */
#ifdef VIRTUAL_EVENT_DEFINITIONS_
#define elif else if
#define null NULL
#define String char*
#endif

LANGUAGE DLLIMPORT CALLING void runVirtualKeyEvent(int eventCode);
LANGUAGE DLLIMPORT CALLING void runVirtualMouseClicEvent(int eventCode);
LANGUAGE DLLIMPORT CALLING void runVirtualMouseMoveEvent(int eventCode, int pixelQuantity);

#if !defined BUILDING
#undef LANGUAGE
#undef DLLIMPORT
#undef CALLING
#endif

#endif
