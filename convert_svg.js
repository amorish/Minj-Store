const fs = require('fs');
const parseSVG = require('svg-path-parser');

const svgStr = fs.readFileSync('shaping_stroke.svg', 'utf8');
const regex = /d="([^"]+)"/g;
let match;
const allPaths = [];

while ((match = regex.exec(svgStr)) !== null) {
  const d = match[1];
  const parsed = parseSVG.makeAbsolute(parseSVG.parseSVG(d));
  
  let currentX = 0;
  let currentY = 0;
  const currentPathCommands = [];

  parsed.forEach(cmd => {
    let out = {};
    if (cmd.code === 'M') {
      out = { type: 'M', x: cmd.x, y: cmd.y };
      currentX = cmd.x; currentY = cmd.y;
    } else if (cmd.code === 'L') {
      out = { type: 'L', x: cmd.x, y: cmd.y };
      currentX = cmd.x; currentY = cmd.y;
    } else if (cmd.code === 'H') {
      out = { type: 'L', x: cmd.x, y: currentY };
      currentX = cmd.x;
    } else if (cmd.code === 'V') {
      out = { type: 'L', x: currentX, y: cmd.y };
      currentY = cmd.y;
    } else if (cmd.code === 'C') {
      out = { type: 'C', x1: cmd.x1, y1: cmd.y1, x2: cmd.x2, y2: cmd.y2, x: cmd.x, y: cmd.y };
      currentX = cmd.x; currentY = cmd.y;
    } else if (cmd.code === 'Q') {
      out = { type: 'Q', x1: cmd.x1, y1: cmd.y1, x: cmd.x, y: cmd.y };
      currentX = cmd.x; currentY = cmd.y;
    } else if (cmd.code === 'Z') {
      out = { type: 'Z' };
    } else {
      console.log('UNHANDLED COMMAND', cmd);
    }
    currentPathCommands.push(out);
  });
  allPaths.push(currentPathCommands);
}

// In the SVG, the paths are from right to left (G N I P A H S), we should reverse it so S is first to match stagger animation correctly!
allPaths.reverse();

fs.writeFileSync('shaping_path.json', JSON.stringify(allPaths));
console.log('Done!');
