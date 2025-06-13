# Changelog

## [Unreleased]

## [0.2.0] - 2025-06-13

### Major Changes

#### Gameplay
- **Added** complete command system with input validation
- **Added** win condition check on 'win' command
- **Added** scoring system with points for key actions
- **Added** hazard counter for blocked movement attempts
- **Added** final score display with bonus points

#### Core Systems
- **Added** player movement system with direction validation
- **Added** item interaction system (tool, crystal)
- **Added** droid blocking mechanics
- **Added** status display showing score and hazard count

### Minor Changes

#### Improvements
- Improved location description formatting
- Updated exit display format in location descriptions
- Streamlined command processing system
- Enhanced player movement feedback

#### Fixes
- Fixed win condition to only trigger on 'win' command
- Prevented game from auto-winning when picking up crystal
- Fixed duplicate messages in terminal output
- Removed automatic tool description printing
- Fixed location connection management
- Corrected typos in location description text
- Fixed Player class method implementations
- Improved error handling in command processing
- Fixed droid blocking mechanics

## [0.1.0] - 2025-06-12

### Major Changes

#### Core Architecture
- **Added** base `StationItem` class for game items
- **Added** `DiagnosticTool` and `EnergyCrystal` classes
- **Added** `Player` class with inventory and location tracking
- **Added** `Location` class for managing game areas
- **Added** `GameController` class for game state management

#### Game Systems
- Implemented basic movement and interaction system
- Added player movement between locations
- Created item interaction system (pick up tool, pick up crystal)
- Added droid interaction using diagnostic tool
- Implemented player status display

### Minor Changes
- Improved class inheritance structure
- Enhanced item examination functionality
- Updated game object initialization parameters
- Improved room information display
- Streamlined item interaction messages
- Fixed various class initialization issues
- Improved code organization and documentation
