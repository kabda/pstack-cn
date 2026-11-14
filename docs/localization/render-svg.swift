// 本地 SVG 可视检查工具；仅读取输入并写入 PNG，不访问网络。
import AppKit
import Foundation
for input in CommandLine.arguments.dropFirst() {
    let url = URL(fileURLWithPath: input)
    guard let image = NSImage(contentsOf: url) else { fatalError("无法读取 SVG：\(input)") }
    let width = Int(image.size.width)
    let height = Int(image.size.height)
    guard let bitmap = NSBitmapImageRep(bitmapDataPlanes: nil, pixelsWide: width, pixelsHigh: height, bitsPerSample: 8, samplesPerPixel: 4, hasAlpha: true, isPlanar: false, colorSpaceName: .deviceRGB, bytesPerRow: 0, bitsPerPixel: 0), let context = NSGraphicsContext(bitmapImageRep: bitmap) else { fatalError("无法创建画布") }
    NSGraphicsContext.saveGraphicsState()
    NSGraphicsContext.current = context
    image.draw(in: NSRect(x: 0, y: 0, width: width, height: height), from: .zero, operation: .sourceOver, fraction: 1)
    NSGraphicsContext.restoreGraphicsState()
    let output = URL(fileURLWithPath: "docs/localization/svg-previews/" + url.lastPathComponent + ".png")
    try bitmap.representation(using: .png, properties: [:])!.write(to: output)
    print("已渲染：\(url.lastPathComponent)，\(width)×\(height)")
}
